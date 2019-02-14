from django.db.models import CharField
from django.db.models import TextField
from django.db import models

# Create your models here.
class detail(models.Model):
    gambar = models.ImageField()
    name = models.CharField(max_length=50)
    harga = models.TextField(max_length=100)

    def __str__(self):
        return self.name