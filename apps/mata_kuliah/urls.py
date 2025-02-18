from django.urls import path 
from . import views


urlpatterns = [
    path('matkul/', views.test, name='test')
]
