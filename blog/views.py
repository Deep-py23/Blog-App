from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from . forms import PostForm

def view_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'view_post.html', {'post':post})



def add_post(request):
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form':form})



def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PostForm(instance=post)
        context = {"form":form, "post":post}
        return render(request, 'add_post.html', context)



def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method=='POST':
        post.delete()
        return redirect('home')

    return render(request, 'delete_confirm.html', {'post':post})




















