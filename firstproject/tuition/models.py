from django.db import models
from django.forms import CharField

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=17)
    content = models.TextField()
