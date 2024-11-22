from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    credits = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.PositiveIntegerField()

    def __str__(self):
        return f"Exam in {self.subject.name} for {self.student.first_name} {self.student.last_name}"
