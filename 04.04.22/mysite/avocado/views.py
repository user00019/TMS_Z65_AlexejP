from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница AVO")

def categories(request, catid):
    print(request.GET)
    return HttpResponse("<h1>Статьи по категориям</h1><p>{catid}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("страница не найдена")

