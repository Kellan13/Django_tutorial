from django.shortcuts import render

# dummy data
posts = [
    {
        'author': 'Kellan Anderson',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': '11/11/21'
    },
    {
        'author': 'Kellan Anderson',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '11/10/21'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
