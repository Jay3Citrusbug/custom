from django.shortcuts import render,redirect
from app1.models import Contact,Custom,Field
from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

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
        
       
        if Contact.objects.filter(phone=phone):
            return JsonResponse({'status':True,'msg':'number is already exists'})
        
     
        
        
        
        current_user = request.user
        current_user_id= current_user.id
        print(current_user_id,"_________________++++)))(((())((()()")
        data_dict =dict(phone=phone,firstname=firstname,lastname=lastname,userid=current_user)
        if birthday:
            datetime_object_birth = datetime.strptime(birthday, '%Y-%m-%d')
            data_dict['bitrh_date'] = datetime_object_birth
        if anniversary:
            datetime_object_anny = datetime.strptime(anniversary, '%Y-%m-%d')
            data_dict['anni_date'] = datetime_object_anny
            
        contactdata=Contact(**data_dict)
        
        
        
      
        contactdata.save()

        last_id=(Contact.objects.last()).id
        print(last_id,"lastid------------")
        
        data=request.POST
        for key in data:
            print(key,"key is ===")
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
        print(pi,"pi is ==========>")
        # pi_custom_field=Custom.objects.all()
        # print(pi_custom_field,"pi_custom_field====================>")
        
   
        
        # for obj in pi_custom_field:
        #     obj.as_dict()
            
        # # dictionaries=[ obj.as_dict() for obj in pi_custom_field ]
        # print(dictionaries,"dictionary is ====================================>>>>>>>")
        # print(type(dictionaries[0]),"dictionary is ====================================>>>>>>>")
        
        datacontext={}
        # new_datacontext={}
        
        # for index, value in enumerate(pi_custom_field):
        #     print(index,"new i is ====>")
        #     print(" new type of i is ====>",(value))
        #     temp={}
        #     temp['id']=value.id,
        #     temp['name']=value.name,
        #     temp['type']=value.type,
            
            
            
            
        #     new_datacontext[f'temp{index}'] = temp
        #     print(temp,"new temp is==>>")
        # print(new_datacontext,"new_Datacontecxt===============>>>>")
         
        for index, value in enumerate(pi):
            # print(index,"i is ====>")
            # print("type of i is ====>",type(value))
            print(value.contact_id.id,"contaact id is =====================>")
            temp={}
            temp['fieldtype']=value.custom_id.type,
            temp['fieldname']=value.custom_id.name,
            temp['fieldvalue']=value.field_value,
            temp['customfieldid']=value.custom_id.id,
            temp['contactfieldid']=value.contact_id.id
            
            
            datacontext[f'temp{index}'] = temp
            print(temp,"temo======>")
            
            # print(value.custom_id.id,"customfield id ============================>")
        # print(datacontext,"datacontext===================>")    
        customcontext={
            'datacontext':datacontext,
            # 'pi_custom_field_json':new_datacontext
            
        }
        print(customcontext,"customcontext=======================>")
        
        return JsonResponse(customcontext,status=200)
        # return HttpResponse(json.dumps({"data": dictionaries})),
@csrf_exempt
def editcontactdata(request):
    if request.method == 'POST':
        print(request)
        print(request.POST,"------POST dasta")
        
        id=request.POST.get('id')
        print(id,"id of student obj data is====>>>>")
        
        contact_obj = Contact.objects.get(id=id)
        print(contact_obj,"object of student is=========>")
        print(contact_obj.lastname,"object of student is firstname=========>")

        
        
        number_edit = request.POST.get('number_edit')
        firstname_edit = request.POST.get('firstname_edit')
        lastname_edit = request.POST.get('lastname_edit')
        birthday_edit = request.POST.get('birthday_edit')
        anniversary_edit = request.POST.get('anniversary_edit')
        # # customclass=request.POST.get('customclass')
        # print(number_edit,"edited number ")
        # print(firstname_edit,"firsstname name edited")
        # print(customclass,"customclass dasta all============================>")
        
        current_user = request.user
        current_user_id= current_user.id
        print(current_user_id,"_________________++++)))(((())((()()")
        
        
        # data_dict =dict(phone=number_edit,firstname=firstname_edit,lastname=lastname_edit,userid=current_user)
        if birthday_edit:
            datetime_object_birth = datetime.strptime(birthday_edit, '%Y-%m-%d')
            # data_dict['bitrh_date'] = datetime_object_birth
        if anniversary_edit:
            datetime_object_anny = datetime.strptime(anniversary_edit, '%Y-%m-%d')
            # data_dict['anni_date'] = datetime_object_anny
            
        # edited_contactdata=Contact(**data_dict)
        
        contact_obj.phone=number_edit
        contact_obj.firstname=firstname_edit
        contact_obj.lastname=lastname_edit
        contact_obj.bitrh_date=datetime_object_birth
        contact_obj.anni_date=datetime_object_anny
        contact_obj.userid=current_user
       
        contact_obj.save()
        
        
        return redirect("listdata")
        # return HttpResponse("all data succssfully")
    



  



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
    



    