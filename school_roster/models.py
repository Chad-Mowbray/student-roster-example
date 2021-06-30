from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"name: {self.name}, date: {self.date_enrolled}"