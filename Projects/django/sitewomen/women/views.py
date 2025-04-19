from django.db.models.fields import return_None
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponse("<h1>Главная страница</h1>")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    if cat_slug == 'old-slug':
        url = reverse('cats', args=('music',))
        return redirect(url)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2023:
            return redirect('home')
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')