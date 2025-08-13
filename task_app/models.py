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
    title = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_do', verbose_name="Статус")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low', verbose_name="Пріоритет")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата виконання")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Коли створено")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks',null=True, blank=True, verbose_name="Ким створено")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Завдання"
        verbose_name_plural="Завдання"