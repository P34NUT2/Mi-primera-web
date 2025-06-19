from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    
    #en el futuro si es que la lanzo pongo esta para que es usuario ponga en que materias son sus fuertes o que le interesa hacer o pedir
    #subject = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True, null=True)

    #para que se ponga imagen en el perfil
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/no-avatar.jpg')

    def __str__(self):
        return f'Perfil de {self.user.username}'
