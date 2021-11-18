from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()  # Pycharm throws error, code still works
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
