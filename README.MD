
### Montar un proyecto en Django con gestion de usuarios  y api con DRF
1. Instalar python 3
2. Entornos virtuales con Pipenv:
    https://www.youtube.com/watch?v=l2_5wiYg5dY

3. Instalar Django

```bash
    pip install django
```

4. Crear proyecto

```bash
    django-admin startproject ejemplo
```

5. Crear app users

```bash
    django-admin startapp user
```
## Crear Modelos
    https://docs.djangoproject.com/en/3.2/topics/db/models/


## Gestion de usuarios

1. Cuando el usuario puede tener un solo rol a la vez, se agrega un campo user_type al modelo Usuario

2. Cuando el usuario puede tener mas de un  rol a la vez, y estos roles son pocos y no cambian con el tiempo, se agrega un campo is_xrol por cada rol que exista a el Modelo Usuario

3. Cuando el usuario puede tener mas de un  rol a la vez, y estos roles cambian con el tiempo se crea una relacion Muchos a Muchos con una tabla de roles.

En este ejemplo se toma la opcion 2, se crea el modelo usuario, estendiendo de  *AbstractUser* y se modufica la variable de configuracion AUTH_USER_MODEL.








### API
    ModelSerializer: Tranforma un usuario de Tipo Modelo y lo transforma en un Json

https://www.django-rest-framework.org/

https://docs.google.com/presentation/d/1rGdR59I3LBn0pBitzdiPhkNr1Nprjp71l64tTndUPmo/edit

https://github.com/developerpe/ecommerce_rest/blob/master/ecommerce_rest/urls.py

https://github.com/pablotrinidad/cride-platzi/blob/master/cride/circles/serializers/__init__.py




https://github.com/SantiagoAndre/talento-colombia/blob/master/src/apps/apis/apps.py




## Autenticacion desde el API con JWT

https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html


