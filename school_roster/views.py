from django.shortcuts import render, redirect
from .models import Student

def all_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'school_roster/all_students.html', context)

def student_detail(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {"student": student}
    return render(request, "school_roster/student_detail.html", context)

def create_student(request):
    if request.method == "GET":
        return render(request, 'school_roster/new_student.html')
    elif request.method == "POST":
        new_name = request.POST["studentname"]
        print(request.POST)
        Student.objects.create(name=new_name)
        return redirect('all_students')