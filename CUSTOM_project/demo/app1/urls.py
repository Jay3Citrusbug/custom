from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('contact/',views.contact,name="contact"),
    path('custom/',views.custom,name="custom"),
    # path('',views.login,name="login")
    path('savedata/',views.savedata,name="savedata"),
    path('fielddata/',views.fielddata,name="fielddata"),

    path('',views.list,name="listdata"),
    path('customlist/',views.customlist,name="customlist"),
    
    path('deletecontact/<int:id>/',views.deletecontact,name="deletecontact"),
    path('editcontact/<int:id>/',views.editcontact,name="editcontact"),

    
]
    