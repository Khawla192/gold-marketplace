from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    picture_url = models.TextField()
    links = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store-detail', kwargs={'store_id': self.id})

class Piece(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    grams = models.CharField(max_length=20)
    karat = models.CharField(max_length=20)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='pieces')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('piece-detail', kwargs={'pk': self.id})
