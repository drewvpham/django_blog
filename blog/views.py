from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
posts = [
    {
        'author': 'DrewP',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 9, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 20, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title': 'About'})
