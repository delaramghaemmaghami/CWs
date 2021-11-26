from django.urls import path
from .views import *

urlpatterns = [
    path("home/", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail")
]
