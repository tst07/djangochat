from django.db import models

# Create your models here.

class Chat(models.Model):
    message = models.CharField(max_length="200")
    author  = models.CharField(max_length="200")
    
    def __str__(self):
        return self.author
