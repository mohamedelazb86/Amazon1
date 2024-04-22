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
            myform=form.save(commit=False)
            myform.user=request.user
            form.save()
            return redirect('/blog/')
    else:
        form=Postform()

    return render(request,'blog/create_post.html',{'form':form})


def update_post(request,id):
    post=Post.objects.get(id=id)
    if request.method =='POST':
        form=Postform(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            form.save()
            return redirect('/blog/')
    else:
        form=Postform(instance=post)



    return render(request,'blog/update_post.html',{'form':form})

def delete_post(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/blog/')