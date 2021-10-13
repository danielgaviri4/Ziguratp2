from rest_framework import viewsets
from rest_framework import filters
from apps.condominium.models import Condominium, SubArea, House, Publication, Communique, CommonArea, Reservation, AdminHistory

from rest_framework.permissions import IsAuthenticated
from apps.api.serializers import CondominiumSerializer, SubAreaSerializer, HouseSerializer, PublicationSerializer, CommuniqueSerializer, CommonAreaSerializer, ReservationSerializer, AdminHistorySerializer


class CondominioView(viewsets.ModelViewSet):
    '''Muestra solo los condominios que son del admin'''
    permission_classes = (IsAuthenticated,)   
    filter_backends = (filters.SearchFilter,) 
    search_fields = ('name','id',)
    # queryset = Condominio.objects.filter(user=usuario authentication)
    serializer_class = CondominiumSerializer
    def get_queryset(self):
        user = self.request.user
        return Condominium.objects.filter(admin=user)

class SubAreaModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)    
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer

class HouseModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)    
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class PublicationModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)    
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class CommuniqueModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)    
    queryset = Communique.objects.all()
    serializer_class = CommuniqueSerializer

class CommonAreaModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)    
    queryset = CommonArea.objects.all()
    serializer_class = CommonAreaSerializer

class ReservationModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)    
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class AdminHistoryModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)    
    queryset = AdminHistory.objects.all()
    serializer_class = AdminHistorySerializer
    

