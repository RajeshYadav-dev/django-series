from django.shortcuts import render
from .models import Student

# Create your views here.

def get_all_students(request):
  students = Student.objects.all()
  return render(request,'student/all_student.html',context={'students':students})
