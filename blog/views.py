from django.shortcuts import render,redirect
from .models import Post
from .form import Postform

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


def create_post(request):
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():

            form.save()
            return redirect('/blog/')
    else:
        form=Postform()

    return render(request,'blog/create_post.html',{'form':form})