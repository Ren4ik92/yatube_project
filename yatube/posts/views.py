from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, any_slug):
    return HttpResponse(f'Групповые посты {any_slug}')
