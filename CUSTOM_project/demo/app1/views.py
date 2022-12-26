from django.shortcuts import render,redirect
from app1.models import Contact,Custom,Field
from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def contact(request):
    return render(request,'client/client_contact.html')

def custom(request):
    return render(request,'client/campaign_settings.html')



@csrf_exempt
def savedata(request):
    if request.method == 'POST':
        print(request)
        print(request.POST,"------POST dasta")
        
        phone = request.POST.get('number')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        birthday = request.POST.get('birthday')
        anniversary = request.POST.get('anniversary')
        
        print(phone,"phone-----------------------------------------------")
        print(birthday,"birthday-------------------------------->")

        # datetime_str = birthday
        # aniver_date=anniversary
        
        # datetime_object = datetime.strptime(datetime_str, '%m-%d')
        # datetime_object_anny = datetime.strptime(aniver_date, '%m-%d')
        
        
        current_user = request.user
        current_user_id= current_user.id
        print(current_user_id,"_________________++++)))(((())((()()")
        

  
      
        
        contactdata=Contact(phone=phone,firstname=firstname,lastname=lastname,bitrh_date=birthday,anni_date=anniversary,userid=current_user)
        
        contactdata.save()

        last_id=(Contact.objects.last()).id
        print(last_id,"lastid------------")
        
        data=request.POST
        for key in data:
            print(key)
            # a=data[key]
            Custom_ID=Custom.objects.get(id=key)
            Contact_ID=Contact.objects.get(id=last_id)
            if data[key] is not None and data[key] != '':
            
                storedata=Field(contact_id=Contact_ID,custom_id=Custom_ID,field_value=data[key])
                print(storedata.field_value,"storedata of value  ")
                print(storedata,"store____________________++++++++++++___________________")
                storedata.save()
            
        return redirect('listdata')

    
# @csrf_exempt
    
# def savefield(request):
#     # dict_data={}
    
#     if request.method == 'POST':
#         data=request.POST
#         print(request.POST)
#         for key in data:
#             print(key)
#             # a=data[key]
#             Custom_ID=Custom.objects.get(id=key)
#             Contacat_ID=Contact.objects.get(firstname='john')
            
#             store=Field(contact_id=Contacat_ID,custom_id=Custom_ID,field_value=data[key])
#             store.save()
            

            

#         # print("My data =",(mydata))
#         return HttpResponse("Hiiiiii")
        
   
    
    
def list(request):
    data=Contact.objects.all()
    custom_field=Custom.objects.all()
    field_data=Field.objects.all()
    # for i in data:
    #     print(i.field_value,"__________fieldvalue_________")
    context={
        'custom_field':custom_field,
        'data':data,
        'field_data':field_data,
        
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
        fielddata=Field.objects.filter(contact_id=id)
        fielddata.delete()
        
        return redirect("listdata")

@csrf_exempt
def editcontact(request):
    if request.method == 'POST':
        print(request.POST,"post request dasta")
        
        id=request.POST.get('sid')
        print(id)
        pi=Field.objects.filter(contact_id=id)
        print(pi,"pi====================>")
        
        # context={
                
        #     }
        datacontext={}
        for index, value in enumerate(pi):
            print(index,"i is ====>")
            print("type of i is ====>",type(value))
            temp={}
            temp['fieldtype']=value.custom_id.type,
            temp['fieldname']=value.custom_id.name,
            temp['fieldvalue']=value.field_value,
            temp['customfieldid']=value.custom_id.id,
            
            datacontext[f'temp{index}'] = temp
            print(temp,"temo======>")
            
            print(value.custom_id.id,"customfield id ============================>")
        print(datacontext,"datacontext===================>")    
        
        return JsonResponse(datacontext,status=200)
       
@csrf_exempt
def editcontactdata(request):
    if request.method == 'POST':
        print(request)
        print(request.POST,"------POST dasta")
        
        number_edit = request.POST.get('number_edit')
        firstname_edit = request.POST.get('firstname_edit')
        lastname_edit = request.POST.get('lastname_edit')
        birthday_edit = request.POST.get('birthday_edit')
        anniversary_edit = request.POST.get('anniversary_edit')
        print(number_edit,"edited number ")
        # customclass=request.POST.get('customclass')
        
        # spiltclass=customclass.split()
        
        print(number_edit,firstname_edit,lastname_edit,"editeddata all============================>")
        
        current_user = request.user
        current_user_id= current_user.id
        print(current_user_id,"_________________++++)))(((())((()()")
        
        edited_contactdata=Contact(phone=number_edit,firstname=firstname_edit,lastname=lastname_edit,bitrh_date=birthday_edit,anni_date=anniversary_edit,userid=current_user)
        edited_contactdata.save()
        
        return redirect("listdata")
    



  



def deletecontactcustom(request,id):

    if request.method=='POST':
        data=Custom.objects.filter(id=id)
        
        print(data)
        data.delete()
        return redirect("customlist")
    
   

def editcontactcustom(request,id):
    if request.method == 'POST':
        fieldname = request.POST.get('fieldname')
        type=request.POST.get('radio')
        print(fieldname,type,"________________________________________________1234")
        
        
        current_user = request.user
        print (current_user.id)
        print(current_user,"_------------________________")
        
        customdata=Custom(id=id,name=fieldname,type=type,userid=current_user)

        customdata.save()
        return redirect("customlist")
    



    