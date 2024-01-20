import json
from django.urls import reverse
from django.test import TestCase
from blogs.models import Blog,Category
from datetime import datetime
from rest_framework.test import APITestCase , APIClient
from rest_framework import status
from django.contrib.auth.models import User 
from datetime import datetime

class TestMain(TestCase):
    
    def test_view_main(self):
        res = self.client.get('')
        self.assertEqual(res.status_code, 200)

    def test_view_detail_page(self):
        category_instance = Category.objects.create(cat='История')
        new_data = Blog.objects.create(id=1,text='HHHH',date=datetime(2222,1,10,11,12),category=category_instance)
        data = Blog.objects.get(id=1)
        self.assertEqual(data.get_absolute_url(),'blogs/1')
    
    def test_view_create_page(self):
        res = self.client.get('/blogs/blogs_create')
        self.assertEqual(res.status_code, 200)
    
    def test_create_page(self):
        category_instance = Category.objects.create(cat='История')
        new_data = Blog.objects.create(id=1,text='HHHH',date=datetime(2222,1,10,11,12),category=category_instance)
        self.assertIsNotNone(new_data)

    def test_view_update_page(self):
        category_instance = Category.objects.create(cat='История')
        new_data = Blog.objects.create(id=1,text='HHHH',date=datetime(2222,1,10,11,12),category=category_instance)
        data = Blog.objects.get(id=1)
        
        res = self.client.get('/blogs/blogs_update/1/')
        
        self.assertEqual(res.status_code, 200)

    def test_view_update_page(self):
        category_instance = Category.objects.create(cat='История')
        new_data = Blog.objects.create(id=1,text='HHHH',date=datetime(2222,1,10,11,12),category=category_instance)
        data = Blog.objects.get(id=1)

        res = self.client.post('/blogs/blogs_update/1/')
        self.assertEqual(res.status_code, 200)


class TestApi(APITestCase , APIClient):
    def setUp(self):
        self.client = APIClient()

        
        self.user = User.objects.create_superuser(
            username="admin",
            password='admin'
        )

        self.category = Category.objects.create(cat='История')

        self.blog = Blog.objects.create(
            text='Test blog',
            image=None,
            date='2024-01-19T07:04:59Z',
            video=None,
            category=self.category
        )
        self.client.force_authenticate(user=self.user)

    def test_view_api_blog(self):
        res = self.client.get('/blogs/blog/')
        self.assertEqual(res.status_code,status.HTTP_200_OK)

    def test_create_api_blog(self):
        url = '/blogs/blogs_create'
        data = {
            'text': 'New blog',
            'image': None,
            'date': '2024-01-20T07:04:59Z',
            'video': None,
            'category': 1
        }
        res = self.client.post(url, json.dumps(data), format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
