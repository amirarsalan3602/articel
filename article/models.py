from django.db import models
from accounts.models import User


class ArticleModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='media')
    creation = models.DateTimeField(auto_now_add=True)
