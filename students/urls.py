# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list_create),
    path('students/<int:pk>/', views.student_detail),
]
