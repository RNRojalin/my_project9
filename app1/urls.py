from app1.views import *
from django.urls import path

app_name='xyz'
urlpatterns=[
    path('a/',a,name='a'),
]