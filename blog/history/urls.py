from django.contrib import admin
from django.urls import path
from history import views
urlpatterns = [
    path('', views.history_page, name='history'),
]

