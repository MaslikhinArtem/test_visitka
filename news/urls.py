from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.news_home, name="home_news"),
]