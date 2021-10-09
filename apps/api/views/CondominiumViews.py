


from rest_framework import viewsets
from apps.condominium.models import Condominium

from rest_framework.permissions import IsAuthenticated
from apps.api.serializers import CondominiumSerializer



class CondominioView(viewsets.ModelViewSet):
    '''Muestra solo los condominios que son del admin'''
    permission_classes = (IsAuthenticated,)    
    # queryset = Condominio.objects.filter(user=usuario authentication)
    serializer_class = CondominiumSerializer
    def get_queryset(self):
        user = self.request.user
        return Condominium.objects.filter(admin=user)