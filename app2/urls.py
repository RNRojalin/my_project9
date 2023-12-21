from app2.views import *
from django.urls import path

app_name='pqr'
urlpatterns=[
    path('b/',b,name='b'),
]