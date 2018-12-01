from django.urls import path
from django.conf.urls import url
from . import views

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('new/', views.PostCreate.as_view(), name='new_article'),

]

