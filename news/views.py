from django.shortcuts import render
from django.template.context_processors import request


def news_home(request):
    return render(request, 'news/news.html' )
