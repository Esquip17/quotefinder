from django.urls import path
from . import views
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('author/<int:pk>', views.author_detail, name='author_detail'),
    path('quote/<int:pk>', views.quote_detail, name='quote_detail'),
    path('author', views.author_list, name='author_list'),
    path('quote', views.quote_list, name='quote_list'),

]
