from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

type_choice = (
    ("text", "text"),
    ("int", "int"),
    ("date", "date"),
    ("largetext","largetext"),
    ("number","number")

)

class Custom(models.Model):
    name = models.CharField(max_length=125)
    type = models.CharField(max_length=125,choices=type_choice)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
     
    def __str__(self):
        return str(self.name)
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            # other stuff
        }
    
    
class Contact(models.Model):
    phone = models.CharField(max_length=10) 
    firstname = models.CharField(max_length=125)
    lastname= models.CharField(max_length=150,null=True,blank=True)
    bitrh_date = models.DateField(blank=True,null=True)
    anni_date = models.DateField(blank=True,null=True)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.firstname)
 
 
class Field(models.Model):
    contact_id=models.ForeignKey(Contact,on_delete=models.CASCADE)
    custom_id=models.ForeignKey(Custom,on_delete=models.CASCADE)
    field_value=models.CharField(default=None,null=True,blank=True,max_length=200)
    