# AI_career_tools

An intelligent web application built with Django and Google Gemini API, designed to help users instantly generate personalized resumes and cover letters tailored to specific job roles, skills, and experience levels.

🚀 Features

✍️ AI-Powered Generation: Uses the Gemini API to craft customized resumes and cover letters.

🧩 Dynamic Templates: Offers multiple professional layouts and styles.

🎯 Contextual Understanding: Generates content based on user input — such as skills, experience, and target job description.

💾 Download Option: Export generated documents in PDF or DOCX formats.

🔒 User Authentication: Secure signup/login system for saving generated documents.

🌐 Responsive UI: Built with Django templates and Bootstrap for smooth user experience.

🧩 Tech Stack

Framework: Django (Python)
Frontend: HTML, CSS, Bootstrap
Backend: Django ORM, SQLite / PostgreSQL
AI Integration: Google Gemini API
Authentication: Django Auth System
Version Control: Git & GitHub

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/ai-resume-builder.git
cd ai-resume-builder


Create a virtual environment:

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up environment variables:
Create a .env file in the project root and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here


Run migrations:

python manage.py migrate


Start the development server:

python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

🧠 How It Works

The user fills out a form with details like name, skills, education, experience, and target job role.

Django sends this structured data to the Gemini API through a backend endpoint.

The AI model returns a tailored resume and cover letter in text format.

The user can preview, edit, and download the generated files.

🧩 Example Output

Input:

Job Role: Data Analyst
Skills: Python, SQL, Power BI, Data Visualization

Output (AI-Generated):

“Data-driven professional skilled in analytical problem-solving, with experience building dashboards and extracting insights from complex datasets…”

📦 Future Enhancements

Add multi-language support

Integrate ATS optimization for better keyword matching

Include AI-based career suggestions

Support custom design themes

🧑‍💻 Author

Ardhendu Bhushan Mishra
Full-Stack Developer | AI & Django Enthusiast
