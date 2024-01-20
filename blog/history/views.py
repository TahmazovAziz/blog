from django.shortcuts import render
from blogs.models import Blog

def history_page(request):
    history = Blog.objects.filter(category__cat='История')
    return render(request,'history.html', {"history":history})