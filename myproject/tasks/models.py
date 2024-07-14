from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    OPCIONES_ESTADO = [
        ('pending', 'Pendiente'),
        ('completed', 'Completado'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=OPCIONES_ESTADO)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True   


class Post(TimeStamped):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username