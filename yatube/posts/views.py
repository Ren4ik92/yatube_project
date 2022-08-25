from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    title = 'Группы'
    context = {
        'text': text,
        'title': title
    }
    return render(request, template, context)
