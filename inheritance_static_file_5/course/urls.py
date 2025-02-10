from django.urls import path
from course.views import python,java

urlpatterns = [
    path('python/',python,name='python'),
    path('java/',java,name='java')
]