from django.shortcuts import render
from school_roster.models import Student
from .models import Grade

def student_grades(request, student_id):
    student = Student.objects.get(id=student_id)
    grades = student.grades.all()
    context = {
        "student": student,
        "grades": grades
    }
    return render(request, "grades/student_grades.html", context)