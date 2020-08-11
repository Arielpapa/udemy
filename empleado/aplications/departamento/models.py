from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=50)
    anulate = models.BooleanField('anulado', default=False )

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering= ['name'] #ordena por orden alfabetico los nombres
        unique_together= ('name','shor_name') #para que no se pueda repetir el nombre no el nombre corto
        

    def __str__(self):
        return  self.name + ' ' + self.shor_name