from django import forms

class CoverLetterForm(forms.Form):
    name = forms.CharField(
        label="Your Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., John Doe'})



    )
    address = forms.CharField(label="Your Address", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 123 Main St'}))
    phone = forms.CharField(label="Your Phone Number", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., +1 234 567 890'}))
    email = forms.EmailField(label="Your Email Address", required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'e.g., you@email.com'}))
    date = forms.CharField(label="Date", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., June 30, 2025'}))
    platform = forms.CharField(label="Platform", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Google Careers website'}))
    industry = forms.CharField(label="Industry/Field", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Technology'}))
    years = forms.CharField(label="Years of Experience", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5'}))
    accomplishment = forms.CharField(label="Accomplishment/Project", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., developed a predictive model...'}))
    ai_project = forms.CharField(label="AI/ML Project", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., recommendation system...'}))


    job_title = forms.CharField(
        label="Job Title",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Software Engineer'})
    )
    company_name = forms.CharField(
        label="Company Name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Google'})
    )
    your_skills = forms.CharField(
        label="Your Key Skills (comma-separated)",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'e.g., Python, Django, JavaScript'})
    )

    job_description = forms.CharField(
        label="Paste Job Description (optional)",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )


from django import forms

TEMPLATE_CHOICES = [
    ('modern', 'Modern'),
    ('classic', 'Classic'),
    ('creative', 'Creative'),
]

class ResumeForm(forms.Form):
    name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Phone", widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="Address", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    education = forms.CharField(label="Education", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g., B.Tech in Computer Science, SRMCEM, 2025'}))
    experience = forms.CharField(label="Work Experience", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g., Internship at XYZ, 2024'}))
    skills = forms.CharField(label="Skills", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g., Python, Django, ML'}))
    projects = forms.CharField(label="Projects", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'e.g., Movie Recommendation System'}))

    job = forms.CharField(label="Job Title", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    company = forms.CharField(label="Company Name", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    job_description = forms.CharField(
        label="Paste Job Description (optional)",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
   
from django import forms

class PortfolioForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    summary = forms.CharField(label="Professional Summary", widget=forms.Textarea(attrs={'class': 'form-control'}))
    projects = forms.CharField(
        label="Projects (one per line, format: Title - Description - Link)",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        help_text="Example: AI Chatbot - Built a chatbot using Python and Gemini - https://github.com/yourrepo"
    )