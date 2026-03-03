Introduction



The AI Personalized Learning Platform is a web-based application developed to provide customized learning recommendations for students based on their academic profile. The system collects information such as weak subjects, learning preferences, and academic goals, and generates structured recommendations to help students improve their performance.



This project demonstrates the practical implementation of backend development, database integration, and rule-based recommendation logic using Python and PostgreSQL.



Problem Statement



In traditional learning environments, students often receive generalized study materials that may not address their individual weaknesses or learning styles. This lack of personalization can reduce learning effectiveness.



The goal of this project is to design and implement a system that:



Identifies student weaknesses



Understands learning preferences



Generates personalized learning recommendations



Provides administrative insights through a dashboard



System Overview



The application is built using a three-layer architecture:



Frontend: HTML and CSS (Flask templates)



Backend: Python using the Flask framework



Database: PostgreSQL



The system includes a rule-based recommendation engine that processes student inputs and generates appropriate course suggestions.



Main Features

Student Module



Submission of academic details



Generation of personalized recommendations



Display of priority level and suggested duration



Admin Module



Role-based login authentication



Dashboard displaying:



Total number of students



Total number of recommendations generated



Most common weak subject



Feedback summary



Recommendation Engine



The recommendation engine analyzes:



Weak subject



Learning style



Academic goal



Based on predefined logic, it suggests structured learning paths.



Project Structure



The repository contains the following main components:



app.py – Main application file containing routes and business logic



db\_config.py – Database connection configuration



recommendation\_engine.py – Logic for generating recommendations



templates/ – HTML template files



static/ – CSS styling files



requirements.txt – Python dependencies



Database Design



The system uses PostgreSQL with the following tables:



students – Stores student details



recommendations – Stores generated recommendations



users – Stores login credentials and roles



feedback – Stores user feedback



Relational constraints ensure proper linkage between students and their recommendations.



Installation and Setup

Step 1: Clone the Repository

git clone https://github.com/Errortree/ai-learning-app.git

cd ai-learning-app

Step 2: Install Dependencies

pip install -r requirements.txt

Step 3: Configure PostgreSQL



Ensure PostgreSQL is installed and running.



Update the database credentials in db\_config.py according to your local setup.



Step 4: Run the Application

python app.py



Open the browser and navigate to:



http://127.0.0.1:5000

Admin Access



Default admin credentials:



Username: admin

Password: admin@123



Testing and Results



The system was tested with multiple student profiles using different weak subjects and learning styles. The application successfully:



Stores student data in the database



Generates appropriate recommendations



Displays aggregated data in the admin dashboard



Maintains role-based authentication



Future Scope



This project can be extended further by:



Integrating a machine learning-based recommendation model



Adding performance analytics and visual dashboards



Implementing student login and tracking progress



Deploying the system on a cloud platform



Developer Information



Developed by: Mohammed Khateeb Arshad

Program: B.Tech – Computer Science and Engineering



Conclusion



The AI Personalized Learning Platform demonstrates how personalized academic recommendations can be generated using structured backend logic and database-driven design. The project reflects practical knowledge of Flask development, PostgreSQL integration, authentication systems, and modular application architecture.

