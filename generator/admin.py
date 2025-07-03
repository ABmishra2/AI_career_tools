from django.contrib import admin
from django.contrib import admin
from .models import CoverLetter , Resume , Portfolio

@admin.register(CoverLetter)
class CoverLetterAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'company', 'created_at')
    search_fields = ('name', 'job', 'company')
    list_filter = ('created_at',)

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'company', 'created_at')
    search_fields = ('name', 'job', 'company')
    list_filter = ('created_at',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
