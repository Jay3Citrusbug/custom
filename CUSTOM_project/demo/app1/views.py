from django.shortcuts import render,redirect
from app1.models import Contact,Custom,Field
from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return render(request,'client/client_contact.html')

def custom(request):
    return render(request,'client/campaign_settings.html')


# def login(request):
#     return render(request,"agency/agency_login.html")




def savedata(request):
    if request.method == 'POST':
        phone = request.POST.get('number')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        birthday = request.POST.get('birthday')
        anniversary = request.POST.get('anniversary')
        
        print(phone,"--------------------------------------------------")

        datetime_str = birthday
        aniver_date=anniversary
        
        datetime_object = datetime.strptime(datetime_str, '%m-%d')
        datetime_object_anny = datetime.strptime(aniver_date, '%m-%d')
        
        
        current_user = request.user
        print (current_user.id)
        print(current_user,"_________________")
        
        data=Contact(phone=phone,firstname=firstname,lastname=lastname,bitrh_date=datetime_object,anni_date=datetime_object_anny,userid=current_user)
        
        data.save()
        return redirect('listdata')

def list(request):
    alldata=Contact.objects.all()
    custom_field=Custom.objects.all()
    context={
        'custom_field':custom_field,
        'data':alldata,
    }
    return render(request,'client/client_contact.html',context)



def fielddata(request):
    if request.method == 'POST':
        fieldname = request.POST.get('fieldname')
        type=request.POST.get('radio')
        print(fieldname,type,"________________________________________________1234")
        
        
        current_user = request.user
        print (current_user.id)
        print(current_user,"_------------________________")
        
        customdata=Custom(name=fieldname,type=type,userid=current_user)

        customdata.save()
    return redirect("customlist")


def customlist(request):
    alldata=Custom.objects.all()

    context={
        'data':alldata,
    }
    print(context)
    return render(request,'client\campaign_settings.html',context)


def deletecontact(request,id):

    if request.method=='POST':
        data=Contact.objects.filter(id=id)
        print(data)
        data.delete()
        context={
            'data':data,
        }
        
        return redirect("listdata")


def editcontact(request,id):
    if request.method == 'POST':
        phone = request.POST.get('number')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        birthday = request.POST.get('birthday')
        anniversary = request.POST.get('anniversary')
        
        print(birthday,anniversary,"--------------------------------------------------")

        datetime_str = birthday
        aniver_date=anniversary
        
        datetime_object = datetime.strptime(datetime_str, '%m-%d')
        datetime_object_anny = datetime.strptime(aniver_date, '%m-%d')
        
        
        current_user = request.user
        
        data=Contact(id=id,phone=phone,firstname=firstname,lastname=lastname,bitrh_date=datetime_object,anni_date=datetime_object_anny,userid=current_user)
        data.save()
        return redirect('listdata')
  


