from turtle import title
from django.db import models
from django.urls import reverse

# Create your models here.

class eventModels(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    eventDescription = models.TextField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("details", args=[str(self.id)])