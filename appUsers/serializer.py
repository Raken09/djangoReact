from rest_framework import serializers
from .models import UsuarioAdmin, UsuarioRegular # Importamos el modelo Task

class UsuarioAdminSerializer(serializers.ModelSerializer): # Convertimos el modelo Task a JSON
    class Meta:
        model = UsuarioAdmin
        fields = '__all__' # Todos los campos serán serializados

class UsuarioRegularSerializer(serializers.ModelSerializer): # Convertimos el modelo Task a JSON
    class Meta:
        model = UsuarioRegular
        fields = '__all__'

