from django.shortcuts import render

# Create your views here.
def python(request):
  return render(request,'course/python.html')

def java(request):
  return render(request,'course/java.html')