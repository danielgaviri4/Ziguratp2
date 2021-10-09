
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from apps.api.serializers import UserSerializer
from apps.api.permissions import UserPermissionsObj
from django.contrib.auth import get_user_model

User = get_user_model()

# class UserSimpleView(views.APIView):
#     def get(self,request):
#         users = User.objects.all()
#         user_serializer = UserSerializer(users, many = True )
#         return Response(user_serializer.data)

class UserModelView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,UserPermissionsObj,)    
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


