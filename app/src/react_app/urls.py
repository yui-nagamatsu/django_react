from django.urls import path
from .views import react_app

urlpatterns =[
    path('', react_app.index, name="index"),
]