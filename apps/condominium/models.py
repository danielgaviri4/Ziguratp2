from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey


from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Condominium(models.Model):
    class Meta:
        verbose_name = 'Condominium'
        verbose_name_plural = 'Condominiums'

    name = models.CharField(max_length=255,unique=True)
    address = models.CharField(max_length=255)
    extension = models.IntegerField(default=0)#extension
    city = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    stratum = models.IntegerField(default=1)
    state = models.BooleanField(default=True)

    admin = models.ForeignKey(User, on_delete=models.CASCADE)


    
    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.name, self.address)

class SubArea(models.Model):
    class Meta:
        verbose_name = 'SubArea'
        verbose_name_plural = 'SubAreas'

    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    
    condominium = models.ForeignKey(Condominium, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.name, self.quantity)


class House (models.Model):
    class Meta:
        verbose_name = 'house'
        verbose_name_plural = 'houses'
    
    num = models.IntegerField(default=0)
    address = models.CharField(max_length=255)

    subArea = models.ForeignKey(SubArea, on_delete=models.CASCADE)
    own = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.num, self.address)

class Publication(models.Model):
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
    
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    date = models.DateField (auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.title, self.text)

class Communique(models.Model):
    class Meta:
        verbose_name = 'Communique'
        verbose_name_plural = 'Communiques'
    
    description = models.CharField(max_length=255)
    date = models.DateField (auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class CommonArea(models.Model):
    class Meta:
        verbose_name = 'CommonArea'
        verbose_name_plural = 'CommonAreas'

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    schedule = models.CharField (max_length=255) #Horario
    method = models.CharField (max_length=255) #metodo de utilizacion
    
    condominium = models.ForeignKey(Condominium, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.name, self.description)

class Reservation(models.Model):
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
    
    identification_card = models.FloatField()
    date = models.DateTimeField()
    reason = models.CharField(max_length=255)
    quantity_people =models.IntegerField (default=1)
    comment= models.CharField (max_length=255)

    commonArea = models.ForeignKey(CommonArea, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.identification_card, self.date)

class AdminHistory (models.Model):
    class Meta:
        verbose_name = 'AdminHistory'
        verbose_name_plural = 'AdminHistories'
    
    star_date = models.DateField ()
    end_date = models.DateField (null=True)
    
    condominium = ForeignKey (Condominium, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] {} | {} |'.format(self.id, self.star_date, self.end_date)