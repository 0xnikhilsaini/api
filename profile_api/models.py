from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.

# class MyUser(AbstractUser):
#     mobile_number = models.CharField(max_length=10, unique=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     def __str__(self):
#        return "{}".format(self.email)







# AUTH_USER_MODEL = 'accounts.MyUser'



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # email = models.EmailField(unique=True,max_length=254,null = True)
    mobile = models.IntegerField(unique=True)
   
    
    def __str__(self):
       return "{}".format(self.user)



# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from django.conf import settings
# from datetime import date
# class User(AbstractUser):
#    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#    email = models.EmailField(_('email address'), unique = True)
#    native_name = models.CharField(max_length = 5)
#    phone_no = models.CharField(max_length = 10)
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

