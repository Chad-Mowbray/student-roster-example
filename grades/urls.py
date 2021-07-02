from django.urls import path
from .views import student_grades

urlpatterns = [
    path("<int:student_id>/", student_grades, name="student_grades")
]