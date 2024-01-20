from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

class Category(models.Model):
    cat = models.CharField(max_length=200)
    

class Blog(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True , null=True)
    date = models.DateTimeField()
    video = models.FileField(upload_to="video/%y" ,null=True, blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return f"blogs/{self.id}"
    

    