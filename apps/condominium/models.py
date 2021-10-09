from django.db import models


from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Condominium(models.Model):
    class Meta:
        verbose_name = 'Condominium'
        verbose_name_plural = 'Condominiums'

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    extension = models.IntegerField(default=0)#extension
    city = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    stratum = models.IntegerField(default=1)
    state = models.BooleanField(default=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)


    
    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.name, self.address)
