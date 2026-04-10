from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo','To Do'),
        ('done','Done'),
    ]
    PRIORITY_CHOICES = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='todo')
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES,default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    