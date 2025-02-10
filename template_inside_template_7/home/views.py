from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request,'home/home.html',context={'name':'Rajesh'})

def about(request):
  return render(request,'home/about.html')

def contact(request):
  return render(request,'home/contact.html')

def service(request):
  return render(request,'home/service.html')