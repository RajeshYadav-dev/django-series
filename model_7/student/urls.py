from django.urls import path
from student.views import get_all_students

urlpatterns = [
    path('all-students/',get_all_students,name='get_all_students')
]