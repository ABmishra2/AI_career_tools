from django.shortcuts import render
from .forms import CoverLetterForm 
import google.generativeai as genai
from django.conf import settings
from . models import CoverLetter , Resume , Portfolio
def index(request):
    cover_letter = None
    autofill = {}
    resume_text = None

    if request.method == "POST":
        form = CoverLetterForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data.get('address', '')
            phone = form.cleaned_data.get('phone', '')
            email = form.cleaned_data.get('email', '')
            date = form.cleaned_data.get('date', '')
            platform = form.cleaned_data.get('platform', '')
            industry = form.cleaned_data.get('industry', '')
            years = form.cleaned_data.get('years', '')
            accomplishment = form.cleaned_data.get('accomplishment', '')
            ai_project = form.cleaned_data.get('ai_project', '')


            job_title = form.cleaned_data['job_title']
            company_name = form.cleaned_data['company_name']
            your_skills = form.cleaned_data['your_skills']

            contact_info = ""
            if name:
                contact_info += name
            if address:
                contact_info += f"\n{address}"
            if phone:
                contact_info += f"\n{phone}"
            if email:
                contact_info += f"\n{email}"
            if date:
                contact_info += f"\n{date}"
            contact_info = contact_info.strip() + "\n\n"




     

            autofill = {
                "name": name,
                "address": address,
                "phone": phone,                   
                "email": email,
                "date": date,
                "platform": platform,
                "industry": industry,
                "years": years,
                "accomplishment": accomplishment,
                "ai_project": ai_project,
                "job_title": job_title,
                "company_name": company_name,
                "your_skills": your_skills,
            }

            # Create the prompt
            prompt = (
                        f"""
                            Write a professional cover letter in this format:

                            [Company Name] Hiring Team
                            [Address, if known, otherwise omit]

                            Dear [Hiring Manager's Name or Hiring Team],

                            Opening Paragraph:
                            State the position you are applying for ({job_title}) at {company_name}, how you found the job (e.g., {platform}), and a one-line hook about why you are a great fit.

                            Middle Paragraph(s):
                            Highlight your relevant skills ({your_skills}), experience ({years} years in {industry}), and projects/accomplishments ({accomplishment}, {ai_project}) that match the job description. Use metrics or outcomes if possible. Show enthusiasm and alignment with the company’s goals or culture.

                            Final Paragraph:
                            Reaffirm your interest in the role. Express your desire for an interview or further discussion. Thank them for their time.

                            Closing & Signature:
                            Use a formal closing (“Sincerely,” or “Best regards,”) and your name ({name}).

                            Please use square bracket placeholders for any missing details, and fill in all provided details.
                            Keep the tone formal, confident, and clear. Limit it to one page.
                            """
                    )
            
            ats_prompt = f"""
You are an ATS (Applicant Tracking System) simulator. 
Evaluate the following resume for clarity, keyword relevance, formatting, and overall strength for a typical recruiter. 
Give a score out of 100 and a brief 1-2 sentence summary of strengths and weaknesses.

Resume:
{resume_text}
"""
            try:
                # Set up Gemini API key
                genai.configure(api_key="AIzaSyCySoBT56IknP79EN5noGf2a7wnP0_xkXM")
                model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

                response = model.generate_content(prompt)
                cover_letter = response.text


                replacements = {
                    '[Your Name/Address]': name + (', ' + address if address else ''),
                    '[Your Phone Number]': phone,
                    '[Your Email Address]': email,
                    '[Date]': date,
                    '[Platform where you saw the advertisement – e.g., Google Careers website]': platform,
                    '[Number]': years,
                    '[Mention relevant industry/field]': industry,
                    '[Mention a specific accomplishment or project highlighting this skill – e.g., developing a predictive model that improved X by Y%]': accomplishment,
                    '[Mention a specific project or achievement demonstrating this skill – e.g., designed and implemented a recommendation system that increased user engagement by Z%]': ai_project,
                    '[Name]': name,
                    '[Job Title]': job_title,
                    '[Company Name]': company_name,
                    '[Skills]': your_skills,
                }
                for placeholder, value in replacements.items():
                    cover_letter = cover_letter.replace(placeholder, value)



                import re

# After your replacements loop:
                cover_letter = re.sub(r'\[.*?\]', '', cover_letter)

                cover_letter = contact_info + cover_letter.lstrip()

                CoverLetter.objects.create(
                    name=name,
                    job=job_title,
                    company=company_name,
                    skills=your_skills,
                    generated_letter=cover_letter
                )

                

            except Exception as e:
                cover_letter = f"Error generating cover letter: {str(e)}"

    else:
        form = CoverLetterForm()

    saved_cover_letters = CoverLetter.objects.all().order_by('-id')

    return render(request, "generator/index.html", {
        "form": form,
        "cover_letter": cover_letter,
        "autofill": autofill,
        "saved_cover_letters": saved_cover_letters,
    })


# Create your views here.
from .forms import ResumeForm
def resume_generator(request):
    resume_text = None
    ats_score = None
    ats_suggestions = None
    extracted_skills = ""
    missing_skills = []
    autofill = {}
    probability = None
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data.get('address', '')
            education = form.cleaned_data['education']
            experience = form.cleaned_data.get('experience', '')
            skills = form.cleaned_data['skills']
            projects = form.cleaned_data.get('projects', '')
            summary = form.cleaned_data.get('summary', '')
            job = form.cleaned_data.get('job', '')
            company = form.cleaned_data.get('company', '')
            job_description = form.cleaned_data.get('job_description', '') 

            # 1. Job Description Analyzer
            if job_description:
                jd_prompt = f"""
Extract the top 5-10 required skills and keywords from this job description as a comma-separated list:
{job_description}
"""
                genai.configure(api_key="AIzaSyCySoBT56IknP79EN5noGf2a7wnP0_xkXM")
                model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
                jd_response = model.generate_content(jd_prompt)
                extracted_skills = jd_response.text.strip()

                # 4. Skill Gap Analysis
                user_skills_set = set([s.strip().lower() for s in skills.split(",")])
                jd_skills_set = set([s.strip().lower() for s in extracted_skills.split(",")])
                missing_skills = list(jd_skills_set - user_skills_set)

            autofill = {
                "name": name,
                "job": job,
                "company": company,
                "skills": skills,
            }

            prompt = f"""
Generate a professional resume in plain text style using the following details:
Name: {name}
Email: {email}
Phone: {phone}
Address: {address}
Professional Summary: {summary}
Education: {education}
Work Experience: {experience}
Skills: {skills}
Projects: {projects}
Format the resume with clear sections and bullet points where appropriate.
"""     
            try:
                genai.configure(api_key="AIzaSyCySoBT56IknP79EN5noGf2a7wnP0_xkXM")
                model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
                response = model.generate_content(prompt)
                resume_text = response.text

                # ATS Score Section
                ats_prompt = f"""
You are an ATS (Applicant Tracking System) simulator. 
Evaluate the following resume for clarity, keyword relevance, formatting, and overall strength for a typical recruiter. 
Give a score out of 100 and a brief 1-2 sentence summary of strengths and weaknesses.
Then, suggest improved content for each of these fields as JSON: summary, skills, experience, education, projects.

Resume:
{resume_text}
"""
                ats_response = model.generate_content(ats_prompt)
                ats_score = ats_response.text.strip()

                # After ats_score is parsed and is a number out of 100
                try:
                    import re
                    score_match = re.search(r'(\d{1,3})', ats_score)
                    probability = int(score_match.group(1)) if score_match else 0
                except Exception:
                    probability = 0

                # Try to extract suggestions as JSON from the response (if present)
                import json, re
                ats_suggestions = None
                match = re.search(r'\{.*\}', ats_score, re.DOTALL)
                if match:
                    try:
                        ats_suggestions = json.loads(match.group())
                    except Exception:
                        ats_suggestions = None

                # Remove JSON from ats_score if present
                if match:
                    ats_score = ats_score.replace(match.group(), '').strip()

                # Save resume to DB
                Resume.objects.create(
                    name=name,
                    job=job,
                    company=company,
                    skills=skills,
                    generated_letter=resume_text
                )
            except Exception as e:
                resume_text = f"Error generating resume: {str(e)}"
                ats_score = "Could not evaluate ATS score."
                ats_suggestions = None
    else:
        form = ResumeForm()
    saved_resumes = Resume.objects.all().order_by('-id')
    return render(request, "generator/resume.html", {
        "form": form,
        "resume_text": resume_text,
        "autofill": autofill,
        "saved_resumes": saved_resumes,
        "ats_score": ats_score,
        "ats_suggestions": ats_suggestions,
        "extracted_skills": extracted_skills,
        "missing_skills": missing_skills,
    })
    return render(request, "generator/resume.html", {"form": form, "resume_text": resume_text})

from django.shortcuts import render
# ...other imports...

def home(request):
    return render(request, "generator/home.html")

# index and resume_generator views remain unchanged

from django.http import JsonResponse


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt  # Only if you have CSRF issues with AJAX, otherwise use CSRF token in JS
def ai_feedback(request):
    if request.method == "POST":
        field_value = request.POST.get("field_value", "")
        field_name = request.POST.get("field_name", "")
        if field_value:
            feedback_prompt = f"Give a brief, actionable tip to improve this {field_name}: {field_value}"
            genai.configure(api_key=settings.GOOGLE_API_KEY)
            model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
            feedback = model.generate_content(feedback_prompt).text.strip()
            return JsonResponse({"feedback": feedback})
    return JsonResponse({"feedback": ""})


from .forms import PortfolioForm
from django.shortcuts import render

def portfolio_builder(request):
    portfolio_html = None
    project_list = []
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            summary = form.cleaned_data['summary']
            projects = form.cleaned_data['projects'].split('\n')
            # Optionally, use AI to enhance summary or project descriptions here

            # Save to database
            Portfolio.objects.create(
                name=name,
                email=email,
                summary=summary,
                projects=projects
            )

            if isinstance(projects, str):
                project_lines = projects.split('\n')
            else:
                project_lines = projects
            project_list = [p.split(' - ') for p in project_lines if p.strip()]

     

            # Render portfolio HTML
            portfolio_html = render(request, "generator/portfolio_template.html", {
                "name": name,
                "email": email,
                "summary": summary,
                "projects": [p.split(' - ') for p in projects if p.strip()],
            }).content.decode()
    else:
        form = PortfolioForm()
    return render(request, "generator/portfolio_builder.html", {
        "form": form,
        "portfolio_html": portfolio_html,
    })