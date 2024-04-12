from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(max_length=200)
    image_name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
