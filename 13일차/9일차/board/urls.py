from django.urls import path
from . import views

urlpatterns =[
    path('index/',views.index, name = "index"),
    path('detail/<spk>', views.detail, name = "detail" ),
    path('create/', views.create, name = "create"),
    path('delete/<spk>', views.delete, name ="delete"),
    path('update/<spk>', views.update, name = "update"),
    path('creply/<spk>',views.creply, name = "creply"),
    path('dreply/<spk><bpk>', views.dreply, name = "dreply"),
]