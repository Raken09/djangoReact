from django.db import models


# Create your models here.
class UsuarioAdmin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class UsuarioRegular(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    fechaLogin = models.DateTimeField(auto_now_add=True)
    duracionLogin = models.IntegerField(default=0)
    clicksBoton1 = models.IntegerField(default=0)
    clicksBoton2 = models.IntegerField(default=0)

    def __str__(self):
        return self.username