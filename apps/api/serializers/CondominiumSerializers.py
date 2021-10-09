

from rest_framework import serializers
from apps.condominium.models import Condominium
'''ModelSerializer: Tranforma un usuario de Tipo Modelo y lo transforma en un Json'''

    


class CondominiumSerializer(serializers.ModelSerializer):
    '''Serializa objeto del condominio'''

    class Meta:
        model = Condominium
        fields = ('id', 'name','address', 'city')
        
    def create(self, validated_data):
        '''Crear y retornar new usuario'''
        # Es necesario escribir esta funcion para que se use la funcion del UserManager Ad
        # print(self.context.request.user)
        user = Condominium.objects.create(admin=self.context['request'].user,**validated_data) # leer sobre *args and **kwars
        return user