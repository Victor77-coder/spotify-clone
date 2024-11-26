from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionamento com o User
    bio = models.TextField(blank=True, null=True)  # Biografia opcional
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Imagem de perfil opcional
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação do perfil
    updated_at = models.DateTimeField(auto_now=True)  # Data de atualização do perfil

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Music(models.Model):
    title = models.CharField(max_length=255)  # Título da música
    artist = models.CharField(max_length=255)  # Nome do artista
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Quem fez o upload
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Data de upload

    def __str__(self):
        return self.title



