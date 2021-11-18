from django.contrib import admin
from django.urls import path, include
from .views import pages
 
urlpatterns = [
    path('', pages, name='pages'),
]
