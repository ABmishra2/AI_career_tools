from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cover-letter/', views.index, name='cover_letter'),
    path('resume/', views.resume_generator, name='resume_generator'),
    path('ai-feedback/', views.ai_feedback, name='ai_feedback'),
    path('portfolio/', views.portfolio_builder, name='portfolio_builder'),



]
