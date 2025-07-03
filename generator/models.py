from django.db import models
from django.db import models

class CoverLetter(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    skills = models.TextField()
    generated_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job} at {self.company}"

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    skills = models.TextField()
    generated_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.job} at {self.company}"
    
from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    summary = models.TextField()
    projects = models.TextField()  # Store as JSON or plain text
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.name} - {self.email}"