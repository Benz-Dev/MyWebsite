from django.shortcuts import render
from blog.models import *
# Create your views here.
def Articles(request):
    articles = Article.objects.filter(visible=True).all()
    context = {
        'articles': articles
    }

    return render(request, 'blog/articles.html', context)

def Post(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article': article
    }

    return render(request, 'blog/article.html', context)

def search_category(request, category):
    articles = Article.objects.filter(categories__name=category).all()

    context = {
        'articles': articles
    }

    return render(request, 'blog/articles.html', context)