from django.contrib.syndication.views import Feed
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
from django.urls import reverse_lazy, reverse

class ArticleListView(ListView):
    template_name = 'blogapp/main.html'
    queryset = (Article.objects.filter(p_d__isnull=False)
                .order_by('-p_d')
                )
    context_object_name = 'obj'

class ArticleDetailView(DetailView):
    template_name = 'blogapp/details.html'
    model = Article
    context_object_name = 'obj'

class LetestArticleField(Feed):
    title = "Blog aticles (lastest)"
    description = "Чтото"
    link = reverse_lazy('blogapp:main_blog')

    def items(self):
        return (Article.objects.filter(p_d__isnull=False)
                .order_by('-p_d')[:5]
                )
    def item_title(self, item: Article):
        return item.title

    def item_description(self, item: Article):
        return  item.body[:200]

