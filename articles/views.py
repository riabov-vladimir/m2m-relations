from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


class ArticleList(ListView):
    model = Article

    template_name = 'articles/news.html'
