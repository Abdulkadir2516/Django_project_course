from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name