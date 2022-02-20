from django.urls import path
from .views import backend

urlpatterns =[
    path('', backend.index, name="index"),
]