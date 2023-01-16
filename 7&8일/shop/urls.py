from django.urls import path
from . import views

urlpatterns= [
    path('index/', views.index, name="index"),
    path('detail/<spk>', views.detail, name="detail"),
    path('delete/<spk>', views.delete, name="delete"),
    path ('create/<spk>', views.create, name = "create"),
    path ('upadate/<spk>', views.update, name = "update")
]