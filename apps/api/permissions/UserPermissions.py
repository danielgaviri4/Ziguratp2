from rest_framework import permissions



class UserPermissionsObj(permissions.BasePermission):
    """
    Owners of the object or admins can do anything.
    Everyone else can do nothing.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return True
        print('evaluando permisos')
        if request.user.is_staff:
            print('es super usuario puede hacer lo que quiera')
            return True
        # solo puede ejecutar la accion si es su informacion
        if obj != request.user:
            print('esta intentando editar informacion de otro usuario')
            return False
        # no puede intentar cambiar su rol

# Api especification
#1. Login:
#                /loging
#                parameters: 2 2
# requires:
#    Nothing

# Create condominio

#                /condominio
#               POST
#                parameters: nombre,asdasd,asd,asd
# requires:
#    rol Administrador

# Ver condominio

#                /condominio
#               POST
#                parameters: nombre,asdasd,asd,asd
# requires:
#    rol Administrador or rol Owner 
#    rol object permission
#ver mis condominios
# Owner





