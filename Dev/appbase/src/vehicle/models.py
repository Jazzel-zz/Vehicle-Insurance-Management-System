from django.db import models
from django.conf import settings
from django.urls import reverse_lazy

# Create your models here.


class Vehicle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    model = models.IntegerField(default=0000)
    rate = models.CharField(max_length=100)
    body_number = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('vehicle:detail', kwargs={'pk': self.pk})
