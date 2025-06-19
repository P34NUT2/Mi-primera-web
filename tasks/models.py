from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripcion")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    
class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', verbose_name="Categoria")
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = RichTextField(verbose_name="Descripcion")
    author = models.ForeignKey(User, on_delete=models.CASCADE)# accedes luego con: task.author.profile.subject
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Precio")
    deadline = models.DateField( verbose_name="Fecha limite")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __str__(self):
        return self.title



