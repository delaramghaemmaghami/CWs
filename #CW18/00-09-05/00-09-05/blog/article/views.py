from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import *


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
