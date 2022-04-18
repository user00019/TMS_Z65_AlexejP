from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.firstname}, {self.lastname}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    studentref = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.pages}'
