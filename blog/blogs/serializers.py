from rest_framework import serializers
from blogs.models import Blog

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','text', 'image', 'date', 'video', 'category']