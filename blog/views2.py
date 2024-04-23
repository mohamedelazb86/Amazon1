from django.shortcuts import render,redirect
from .models import Post
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView

class Post_list(ListView):
    model=Post
    template_name='blog/post_list.html'


class Post_detail(DetailView):
    model=Post
    template_name='blog/post_detail.html'

class Post_Create(CreateView):
    model=Post
    fields='__all__'
    template_name='blog/create_post.html'
    success_url='/blog/'

class Post_update(UpdateView):
    model=Post
    fields='__all__'
    
    template_name='blog/update_post.html'
    success_url='/blog/'

class Post_Delete(DeleteView):
    model=Post
    template_name='blog/delete_post.html'
    success_url='/blog/'