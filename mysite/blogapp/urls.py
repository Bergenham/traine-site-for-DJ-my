from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
    LetestArticleField
)

app_name = 'blogapp'

urlpatterns = [
    path('', ArticleListView.as_view(), name='main_blog'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail_blog'),
    path('ss/', LetestArticleField(), name="a_f")
]