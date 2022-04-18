from django.contrib import admin
from bbb.models import Book, Student

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ("firstname", "lastname")


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'pages', 'studentref')


