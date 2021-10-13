from django.contrib import admin
from .models import Condominium, Publication, SubArea, House, CommonArea, Communique, AdminHistory, Reservation

# Register your models here.

admin.site.register(Condominium)
admin.site.register(SubArea)
admin.site.register(House)
admin.site.register(Publication)
admin.site.register(CommonArea)
admin.site.register(Communique)
admin.site.register(AdminHistory)
admin.site.register(Reservation)