from django.db import models
from django.conf import settings #helps to use user model dynamically
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, # linking to custom user model in account
        on_delete=models.CASCADE, # if user deleted -> blog deleted
        related_name='blogs'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"

