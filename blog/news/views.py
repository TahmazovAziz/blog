from django.shortcuts import render
from blogs.models import Blog

def news_page(request):
    news = Blog.objects.filter(category__cat='Новости')
    return render(request,'news.html', {"news":news})