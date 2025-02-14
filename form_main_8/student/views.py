from django.shortcuts import render
from student.form import Registeration, Login

# Create your views here.

def registration(request):
  register_form = Registeration()
  return render(request,'student/register.html',{'form':register_form})

def login(request):
  # login_form = Login(auto_id=True) # same as variable name eg email as email
  # login_form = Login(auto_id=False) # here label will be remove
  login_form = Login(auto_id=True)
  return render(request,'student/login.html',{'form':login_form})
