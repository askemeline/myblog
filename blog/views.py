from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone



from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('post_title')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

class PostCreate(CreateView):
    model = Post
    template_name = 'blog/new_article.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(PostCreate, self).form_valid(form)


    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.post_author = self.request.user
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
