from django.test import TestCase, Client
from django.urls import reverse
from school_roster.models import Student
from .models import Grade


class TestGradesModels(TestCase):

    fixtures = ["grade_fixtures.json"]

    def test_bob_exists(self):
        bob = Student.objects.get(pk=1)
        self.assertEqual(bob.name, "Bob")

    def test_bobs_grades(self):
        bob = Student.objects.get(pk=1)
        bobs_grades = bob.grades.all()
        self.assertEqual(bobs_grades.count(), 2)
        self.assertEqual([grade.letter for grade in list(bobs_grades)], ["A", "B"])


    def test_first_student_grades_template(self):
        # resp = self.client.get("/grades/1/")
        resp = self.client.get(reverse("student_grades", args=[1]))
        self.assertTemplateUsed(resp, "grades/student_grades.html")

    def test_first_student_200_response(self):
        resp = self.client.get(reverse("student_grades", args=[1]))
        self.assertEqual(resp.status_code, 200)