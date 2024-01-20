from django.shortcuts import render
from blogs.serializers import BlogSerializers
from rest_framework import viewsets
from blogs.models import Blog
 
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers