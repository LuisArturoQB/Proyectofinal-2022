from django.db import models

# Create your models here.

class zapatos(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='zapatos')
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='zapato'
        verbose_name_plural='zapatos'

    def __str__(self):
        return self.titulo
