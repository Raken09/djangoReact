from django.contrib import admin
from .models import UsuarioAdmin, UsuarioRegular

# Register your models here.
admin.site.register(UsuarioAdmin)
admin.site.register(UsuarioRegular)