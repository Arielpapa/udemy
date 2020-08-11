from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField
# Create your models here.

class Habilidades(models.Model):
    habilidades = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return  self.habilidades


class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )

    first_name = models.CharField('Nombres',max_length=50)
    last_name = models.CharField('Apellido',max_length=50)
    full_name= models.CharField('Nombre completo',max_length=120,blank=True)
    job = models.CharField('Trabajo', max_length=5, choices= JOB_CHOICES )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField('Habilidades')
    hoja_vida= RichTextField(blank=True)

    class Meta:
        verbose_name = 'Mi personal'
        verbose_name_plural = 'Area personal de la empresa'
        ordering= ['last_name'] #ordena por orden alfabetico los nombres
        unique_together= ('first_name','last_name') #para que no se pueda repetir el nombre no el nombre corto
    

    def __str__(self):
        return str(self.id) + ' ' + self.first_name + ' ' + self.last_name 