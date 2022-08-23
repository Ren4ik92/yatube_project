from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, any_slug):
    return HttpResponse(f'Групповые посты {any_slug}')
