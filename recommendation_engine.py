def generate_recommendation(student):

    class_level = student["class_level"]
    subject = student["weak_subject"]
    style = student["learning_style"]
    goal = student["goal"]

    score = 40

    score += class_level * 2

    if "exam" in goal.lower():
        score += 15

    if style.lower() == "practice":
        score += 10
    elif style.lower() == "videos":
        score += 6

    if score > 100:
        score = 100

    if score >= 80:
        level = "Advanced"
    elif score >= 60:
        level = "Intermediate"
    else:
        level = "Foundation"

    confidence = round((score / 100) * 0.9, 2)
    duration = 6 + (score // 25)

    return {
        "course": f"{subject} {level} Learning Program",
        "priority": "High" if score > 65 else "Medium",
        "duration": f"{duration} Weeks",
        "difficulty_index": score,
        "confidence": confidence
    }