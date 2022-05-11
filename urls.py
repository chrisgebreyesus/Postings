from django.urls import path
from . import views

urlpatterns = [
 path('', views.get_home, name='home'),
 path('about/', views.get_about, name='about'),
 path('posts/', views.get_posts, name='posts'),
 path('post/<int:post_id>/', views.get_post, name='post'),
]