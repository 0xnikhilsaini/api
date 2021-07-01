from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Apikey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name  =  models.CharField(max_length=60)
    app_key  =  models.CharField(max_length=255)
    market_key  = models.CharField(max_length=255)
    app_sacret  = models.CharField(max_length=255)
    market_sacret  = models.CharField(max_length=250)
    type  =  models.CharField(max_length=255)
    create_at  = models.DateField(auto_now_add=True) 
    Copy_percent = models.CharField(max_length=50)

    
   

    def __str__(self):
         return self.client_name

#   GENDER = (
#         ('M', 'Homme'),
#         ('F', 'Femme'),
#     )

#  gender = models.CharField(max_length=1, choices=GENDER)


    # class apikey(models.Model):
    # client = models.ForeignKey(User, on_delete=CASCADE)
    # appsacret = models.CharField(max_length=50)
    # marketsecret = models.CharField(max_length=50)
    # create_at = models.DateTimeField(auto_now_add=True)
    # # update_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.appsacret






    # class Apikey(models.Model):
    # client_name = CharField(max_length=150)
    # appkey = CharField(max_length=130)
    # marketkey = CharField(max_length=130)
    # appsecret = CharField(max_length=140)
    # marketsecret = CharField(max_length=120)
    # type = CharField(max_length=120)
    # created_at =  create_at = models.DateTimeField(auto_now_add=True)
    # userid = models.ForeignKey(User, on_delete=models.CASCADE)




