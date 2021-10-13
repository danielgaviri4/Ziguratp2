# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.db import models

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_admin =models.BooleanField(default = False,null=False)
    is_owner =models.BooleanField(default = False,null=False)
    is_lessee =models.BooleanField(default = False,null=False)#Arrendatario
    email = models.EmailField(unique=True,null=False)
    identification_card = models.CharField(max_length=25, null=False)
    phone = models.CharField(max_length=50)
    # another userdata
    def __eq__(self,other):
        return  self.email == other.email
    def __hash__(self):
        return super(User,self).__hash__()
    # @property
    # def is_admin(self):
    #     return self.is_superuser or self.is_admin
    # @property
    # def is_owner(self):
    #     return self.is_superuser or self.is_owner



