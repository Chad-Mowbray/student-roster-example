from django.test import TestCase, Client
from django.urls import reverse
from .models import Student

class BasicTestRoster(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.s1 = Student.objects.create(name="Bob")
        cls.s2 = Student.objects.create(name="Jane")


class TestRosterModels(BasicTestRoster):

    def test_student_string(self):
        first = Student.objects.get(pk=1)
        print(first)
        self.assertIn("name: Bob", str(first))

    def test_add_new_student(self):
        all_students = Student.objects.all()
        self.assertEqual(all_students.count(), 2)
        Student.objects.create(name="Sally")
        all_students = Student.objects.all()
        self.assertEqual(all_students.count(), 3)


class TestRosterViews(BasicTestRoster):

    def setUp(self):
        self.client = Client()

    def test_all_returns_200(self):
        resp = self.client.get("/roster/all/")  
        self.assertEqual(resp.status_code, 200)

    def test_all_returns_template(self):
        resp = self.client.get(reverse("all_students"))
        self.assertTemplateUsed(resp, 'school_roster/all_students.html')

    def test_first_student_in_all(self):
        resp = self.client.get(reverse("all_students"))
        self.assertContains(resp, "name: Bob", html=True)

    def test_post_request_redirects(self):
        body = {
            "studentname": "Sally"
        }
        resp = self.client.post(reverse("create_student"), body)
        self.assertRedirects(resp, reverse("all_students"))

    def test_post_updates_db(self):
        body = {
            "studentname": "Sally"
        }
        resp = self.client.post(reverse("create_student"), body) 
        new_student = Student.objects.get(name="Sally")
        self.assertEqual(new_student.name, "Sally")