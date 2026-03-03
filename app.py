from flask import Flask, render_template, request, redirect, session
from db_config import get_connection
from recommendation_engine import generate_recommendation
from textblob import TextBlob

app = Flask(__name__)
app.secret_key = "adaptive_learning_secret"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if "role" in session:
        if session["role"] == "admin":
            return redirect("/admin")
        return redirect("/")

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"].strip()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT role FROM users WHERE username=%s AND password=%s",
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session["role"] = user[0]
            session["username"] = username

            if user[0] == "admin":
                return redirect("/admin")
            else:
                return redirect("/")

        return "Invalid Credentials"

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/submit", methods=["POST"])
def submit():

    student_data = {
        "name": request.form["name"],
        "class_level": int(request.form["class_level"]),
        "weak_subject": request.form["weak_subject"],
        "learning_style": request.form["learning_style"],
        "goal": request.form["goal"]
    }

    recommendation = generate_recommendation(student_data)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, class_level, weak_subject, learning_style, goal)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """, (
        student_data["name"],
        student_data["class_level"],
        student_data["weak_subject"],
        student_data["learning_style"],
        student_data["goal"]
    ))

    student_id = cursor.fetchone()[0]

    cursor.execute("""
        INSERT INTO recommendations (student_id, course, priority, duration)
        VALUES (%s, %s, %s, %s)
    """, (
        student_id,
        recommendation["course"],
        recommendation["priority"],
        recommendation["duration"]
    ))

    conn.commit()
    cursor.close()
    conn.close()

    recommendation["student_id"] = student_id

    return render_template("result.html", rec=recommendation)


@app.route("/feedback", methods=["POST"])
def feedback():

    student_id = request.form["student_id"]
    feedback_text = request.form["feedback"]

    polarity = TextBlob(feedback_text).sentiment.polarity

    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO feedback (student_id, feedback_text, sentiment)
        VALUES (%s, %s, %s)
    """, (student_id, feedback_text, sentiment))

    conn.commit()
    cursor.close()
    conn.close()

    return f"Feedback recorded. Sentiment: {sentiment}"


@app.route("/admin")
def admin():

    if "role" not in session or session["role"] != "admin":
        return redirect("/login")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM recommendations")
    total_recommendations = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM feedback WHERE sentiment='Negative'")
    negative_cases = cursor.fetchone()[0]

    cursor.execute("""
        SELECT sentiment, COUNT(*)
        FROM feedback
        GROUP BY sentiment
    """)
    sentiment_data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "admin.html",
        total_students=total_students,
        total_recommendations=total_recommendations,
        negative_cases=negative_cases,
        sentiment_data=sentiment_data
    )


if __name__ == "__main__":
    app.run(debug=True)