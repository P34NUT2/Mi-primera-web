from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task  # Ajusta si tu app de tareas tiene otro nombre

class Offer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='offers')#el related name sirve para acceder desde otro modelo relacionado a este
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='offers_made')
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Offer by {self.user.username} on {self.task.title} - {self.status}"
