from django.urls import path
from . import views

#! kenapa harus membuat urls pada setiap app, agar pemanggilan path pada urls root bisa lebih efisien

urlpatterns = [
    path("", views.main, name="main"),
    path('data-dosen/', views.show_data_dosen, name='data_dosen'),
    path('data-dosen/details/<int:id>', views.details, name="details"),
    path("testing/", views.testing, name="testing")
]
