from email.policy import default
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.forms import CharField
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=17)
    content = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student')
    )

    MEDIUM = (
        ('Bangla', 'Bangla'),
        ('English', 'English'),
        ('Urdu', 'Urdu'),
        ('Hindi', 'Hindi'),
        ('Arabic', 'Arabic')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salary = models.FloatField()
    details = models.TextField()
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(default='tuition/images/default.jpg', upload_to='tuition/images')
    medium = MultiSelectField(max_length=100, max_choices=5, choices=MEDIUM, default='Bangla')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

