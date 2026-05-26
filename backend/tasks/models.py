from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STAGE_CHOICES = [
        ('todo', 'Todo'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
