from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Caracteristica(models.Model):
    producto = models.ForeignKey(Producto, related_name='caracteristicas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nombre}: {self.valor}"

