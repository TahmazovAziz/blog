from django.contrib import admin
from django.urls import path,include
from main import views
from rest_framework import routers
from blogs.views import BlogViewSet
router = routers.DefaultRouter()
router.register(r'blog' , BlogViewSet)
urlpatterns = [
    path('<int:pk>/' , views.BlogDetailView.as_view(), name='blog'),
    path('blogs_create' , views.create_blog , name='blogs_create'),
    path('blogs_update/<int:pk>/' , views.BlogUpdateView.as_view(), name='blogs_update'),
    path('',include(router.urls)),
    

]

urlpatterns += router.urls