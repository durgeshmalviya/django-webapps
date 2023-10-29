
from django.urls import path
from . import views

urlpatterns =[
path('', views.blog, name= 'blog'),
path('home', views.home, name= 'index'),
path('<int:pk>/', views.blog_detail, name='blog_detail'),

]