from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(null=False,blank=True, default="", editable=False, unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} {self.date}"

