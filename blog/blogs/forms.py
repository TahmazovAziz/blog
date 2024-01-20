from blogs.models import Blog
from django.forms import ModelForm , TextInput ,DateTimeInput , Textarea

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['text', 'image', 'date', 'video', 'category']

        widgets = {
            "text":Textarea(attrs={
                'class':'form-control',
                'placeholder':'Названия вашего поста',

            }),
            "date":DateTimeInput(attrs={
                'class':'form-control',
                'type':'datetime-local',
                'placeholder':'Время публикации',
                
            })
        }