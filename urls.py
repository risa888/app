from django.urls import path
from . import views
from risapp.views import article_view,article_create_view,comments_create,comments_view
from blog.views import product_detail_view


urlpatterns = [
    path('article', views.article_view, name='article'),
    path('create', article_create_view, name='create'), 
    path('comment', comments_create, name='comment'),
    path('comm', comments_view, name='comm'),
]