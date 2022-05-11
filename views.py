from django.shortcuts import render
from .models import Post, Condition, Category

def get_home(request):
    return render (request, 'home.html')

def get_about(request):
    return render (request, 'about.html')

def get_posts(request):
    all_posts = Post.objects.all()
    data = { 'posts': all_posts }
    return render (request, 'posts.html', data)

def get_post(request, post_id ):
    a_post = Post.objects.get(id=post_id)
    data = { 'post': a_post }
    return render (request, 'post.html', data)
# Create your views here.
