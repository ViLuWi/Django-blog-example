from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    title   = models.CharField(max_length=120)
    content = models.TextField(max_length=5000)
    image   = models.ImageField(null=True, blank=True, upload_to='post')