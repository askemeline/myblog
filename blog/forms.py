from django.forms import ModelForm
from django.db import models
from blog.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
