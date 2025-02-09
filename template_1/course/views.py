from django.shortcuts import render

# Create your views here.
def python(request):
  course_detail = {'name':'python','duration':'1-year','tutor':'Rajesh Yadav'}
  return render(request,'course/python.html',context={'data':course_detail})

def java(request):
  course_detail = {'name':'java','duration':'2-year','tutor':'Rakesh Yadav'}
  return render(request,'course/java.html',context={'data':course_detail})
