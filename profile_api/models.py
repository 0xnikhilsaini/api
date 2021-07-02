from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # email = models.EmailField(unique=True,max_length=254,null = True)
    mobile_number = models.CharField(max_length=10, unique=True, null=True)
   
    
    def __str__(self):
       return "{}".format(self.user)





