from django.urls import path

# my views
from .views import Home1 , Home2

urlpatterns = [
    
    path('',Home1,name='home1'),
    path('home2',Home2,name='home2')
]
