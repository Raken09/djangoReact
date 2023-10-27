from rest_framework import viewsets
from .serializer import UsuarioAdminSerializer, UsuarioRegularSerializer
from .models import UsuarioAdmin, UsuarioRegular


# Create your views here.
# las vistas son las que se encargan de procesar las peticiones y devolver una respuesta al cliente
class UsuarioAdminView(viewsets.ModelViewSet): 
    serializer_class = UsuarioAdminSerializer
    queryset = UsuarioAdmin.objects.all()

class UsuarioRegularView(viewsets.ModelViewSet): 
    serializer_class = UsuarioRegularSerializer
    queryset = UsuarioRegular.objects.all()
