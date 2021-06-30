from django.urls import path
from .views import all_students, student_detail, create_student

urlpatterns = [
    path('all/', all_students, name="all_students"),
    path("<int:student_id>/", student_detail, name="student_detail"),
    path("new/", create_student, name="create_student")
]