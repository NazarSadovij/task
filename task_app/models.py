from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікуєця'),
        ('in_progress', 'В процесі'),
        ('Done', 'Виконано')
    ]
    PRIORITY_CHOICES=[
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий')
    ]
    title = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(null=True, blank=True, verbose_name='Опис')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='.')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name='.')
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', verbose_name='.')

    def __str__(self):
        return self.title