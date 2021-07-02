from django.db import models
from school_roster.models import Student


class Grade(models.Model):
    letter = models.CharField(max_length=1, unique=True)
    students = models.ManyToManyField(Student, related_name="grades")

    def __str__(self):
        return f"grade: {self.letter}"
