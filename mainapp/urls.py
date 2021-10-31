from django.contrib import admin
from django.urls import path, include
from .views import home, post
urlpatterns = [
    path('', home),
    path('post/<id>', post)
]
