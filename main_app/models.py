from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    picture_url = models.URLField(blank=True, null=True)
    links = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
