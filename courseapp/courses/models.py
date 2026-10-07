from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False,blank=True, default="", editable=True, unique=True, db_index=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='img', default="")
    date = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(null=False,blank=True, default="", editable=True, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.title} {self.date}"

class UploadModel(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)