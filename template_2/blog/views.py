from django.shortcuts import render

# Create your views here.
def facebook(request):
  return render(request,'blog/facebook.html') 

def instagram(request):
  return render(request,'blog/instagram.html') 