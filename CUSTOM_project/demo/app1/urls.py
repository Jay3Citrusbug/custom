from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('contact/',views.contact,name="contact"),
    path('custom/',views.custom,name="custom"),
    # path('',views.login,name="login")
    path('savedata/',views.savedata,name="savedata"),
    # path('savefield/',views.savefield,name="savefield"),

    path('fielddata/',views.fielddata,name="fielddata"),

    path('',views.list,name="listdata"),
    # path('contactdata/',views.list,name="listdata"),
    path('customlist/',views.customlist,name="customlist"),
    
    path('deletecontact/<int:id>/',views.deletecontact,name="deletecontact"),
    path('editcontact/',views.editcontact,name="editcontact"),
    path('editcontactdata/',views.editcontactdata,name="editcontactdata"),
    path('deletecontactcustom/<int:id>/',views.deletecontactcustom,name="deletecontactcustom"),
    path('editcontactcustom/<int:id>/',views.editcontactcustom,name="editcontactcustom"),


    
]
    