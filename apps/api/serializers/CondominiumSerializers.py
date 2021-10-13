from django.db.models import fields
from rest_framework import serializers
from apps.condominium.models import Condominium, SubArea, House, Publication, Communique, CommonArea, Reservation, AdminHistory
'''ModelSerializer: Tranforma un usuario de Tipo Modelo y lo transforma en un Json'''

    


class CondominiumSerializer(serializers.ModelSerializer):
    '''Serializa objeto del condominio'''

    class Meta:
        model = Condominium
        fields = ('id', 'name','address', 'extension', 'city', 'department','stratum','state','admin')
        

class SubAreaSerializer(serializers.ModelSerializer):
    '''Serializa el objeto de la sub area'''
    class Meta:
        model = SubArea
        fields = ('id', 'name','quantity', 'condominium')
    
class HouseSerializer(serializers.ModelSerializer):
    '''serializa la vivienda'''
    class Meta:
        model = House
        fields = "__all__"

class PublicationSerializer(serializers.ModelSerializer):
    '''serializa la Publicacion'''
    class Meta:
        model = Publication
        fields = "__all__"

class CommuniqueSerializer(serializers.ModelSerializer):
    '''serializa el Comunicado'''
    class Meta:
        model = Communique
        fields = "__all__"

class CommonAreaSerializer(serializers.ModelSerializer):
    '''serializa el area comun'''
    class Meta:
        model = CommonArea
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    '''serializa la reservacion'''
    class Meta:
        model = Reservation
        fields = "__all__"

class AdminHistorySerializer(serializers.ModelSerializer):
    '''serializa la reservacion'''
    class Meta:
        model = AdminHistory
        fields = "__all__"