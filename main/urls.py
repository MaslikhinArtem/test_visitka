
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name='about'),
    path('forum', views.forum, name='forum'),
    path('form', views.form, name='form'),
    path('bk_vilka', views.bk_vilka, name='vilka'),
    # path('create', views.create, name='create')
]