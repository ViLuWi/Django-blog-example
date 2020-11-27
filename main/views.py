from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .forms import PostForm


def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {
        'posts': post
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {
        'form': form
    })


def new_post(request):
    if request.method == 'POST':  # when clicking the submit button
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)  # prevent saving to Database
            form.instance.author = request.user  # set author to logged in user
            form.save()  # save to Database
            return redirect('index')
    else:
        form = PostForm()

    if request.user.is_authenticated:  # check if user is logged in
        return render(request, 'new-post.html', {
            'form': form
        })
    else:  # if the user is not logged in, redirect to the index
        return redirect('index')
