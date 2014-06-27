from django.db import models

# Create your models here.

class Producto(models.Model):

    Nombre = models.CharField(max_length = 50)
    Precio = models.IntegerField(max_length = 50)
    Cantidad = models.FloatField(max_length = 50)

    def __unicode__(self):
        return self.Nombre
