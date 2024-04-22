from django.shortcuts import render
from .models import Post

def post_list(request):
    data=Post.objects.all()
    context={
        'posts':data
    }
    return render(request,'blog/post_list.html',context)
    

def post_detail(request,slug):
    post=Post.objects.get(slug=slug)

    context={
        'post':post
    }
    return render(request,'blog/post_detail.html',context)
