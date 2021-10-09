

from rest_framework import serializers

'''ModelSerializer: Tranforma un usuario de Tipo Modelo y lo transforma en un Json'''

from django.contrib.auth import get_user_model
# from apps.users.models import User
User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # include = ('is_admin','email')
#         exclude = []

    


class UserSerializer(serializers.ModelSerializer):
    '''Serializa objeto del usuario'''

    class Meta:
        model = User
        fields = ('id', 'username','email', 'first_name', 'password','is_admin','is_owner')
        '''Para que no muestre la clave al momento de consultar'''
        extra_kwargs= {
            'password':{
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }
    # def get_the_required_fields(self, ....):
    #     user = self.request.user
    #     if user.is_superuser and (viewtype is ListCreateAPIView):
    #         return super_user_list_fields
    #     if user.is_superuser and (viewtype is RetrieveUpdateDestroyAPIView):
    #         return super_user_detail_fields
    def create(self, validated_data):
        '''Crear y retornar new usuario'''
        # Es necesario escribir esta funcion para que se use la funcion del UserManager Ad
        user = User.objects.create_user(**validated_data) # leer sobre *args and **kwars
        return user
    
    def update(self, instance, validated_data):
        '''actualiza usuario'''
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)