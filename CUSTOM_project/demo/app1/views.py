from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request,'client/client_contact.html')

def custom(request):
    return render(request,'client/campaign_settings.html')


def login(request):
    return render(request,"agency/agency_login.html")

