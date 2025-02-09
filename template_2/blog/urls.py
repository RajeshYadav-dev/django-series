from django.urls import path
from blog.views import facebook,instagram

urlpatterns = [
    path('facebook/', facebook,name='facebook'),
    path('instagram/',instagram,name='instagram'),
]
