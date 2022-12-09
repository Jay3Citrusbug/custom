from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('contact/',views.contact,name="contact"),
    path('custom/',views.custom,name="custom"),
    path('',views.login,name="login")

    
]
    