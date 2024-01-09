from django.db import models

# Create your models here.
class ModeloBlog(models.Model):
    autor=models.CharField(max_length=100)
    titulo=models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to='imagenes/', null=True, blank=True)
    fecha=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
