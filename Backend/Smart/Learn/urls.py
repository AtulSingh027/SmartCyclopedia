from django.urls import path
from Learn import views

urlpatterns = [
    path('Subjectspage', views.Subjectspage),
    path('Subjectsget', views.Subjectsget),  # API endpoint for Subjects
]
