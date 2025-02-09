from django.shortcuts import render

# Create your views here.
def facebook(request):
  detail = {'name':'Rajesh'}
  return render(request,'blog/facebook.html',context=detail) 

def instagram(request):
  details = {'name':'Rajesh','age':23,'city':'delhi'}
  desc = {'desc':'Hello Rajesh Yadav how are you.'}
  return render(request,'blog/instagram.html',context={'details':details,'desc':desc}) 