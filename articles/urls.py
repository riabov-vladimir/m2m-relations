
from django.conf.urls import url
from django.urls import path

from articles.views import ArticleList

urlpatterns = [
    path('', ArticleList.as_view()),
]


print('artcls/url triggered =================================')