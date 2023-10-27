from django.core.management.base import BaseCommand
from appUsers.models import UsuarioAdmin, UsuarioRegular

class Command(BaseCommand):
    help = 'Crea un usuario admin y 35 usuarios regulares'

    def handle(self, *args, **kwargs):
        admin_user = UsuarioAdmin(username='admin', password='admin_password')
        admin_user.save()

        for i in range(1, 36):
            username = f'user{i}'
            password = f'password{i}'
            user = UsuarioRegular(username=username, password=password)
            user.save()

        self.stdout.write(self.style.SUCCESS('Usuarios creados con éxito'))
