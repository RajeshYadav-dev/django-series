from django.urls import path
from course.views import python

urlpatterns = [
    path('python/',python,name='python')
]