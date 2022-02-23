from django.urls import path
from .views import backend
from django.urls import reverse


from .views import backend


app_name = 'backend'
urlpatterns =[
    path('', backend.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', backend.DetailView.as_view(), name='detail'),
]

