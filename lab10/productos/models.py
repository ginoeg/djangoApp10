from django.db import models

# Create your models here.
class Producto(models.Model):

    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(decimal_places=3, max_digits=6)
    imagen=models.ImageField(upload_to="imagenes",null=True)
    
    
