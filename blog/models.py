import datetime

from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

