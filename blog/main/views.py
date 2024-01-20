from django.shortcuts import render
from blogs.models import Blog
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from blogs.forms import BlogForm
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'main/main.html', {'blogs':blogs})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
        else:
            print('asd')
    form = BlogForm() 
    data={
        'form':form
    }
    return render(request, 'main/create.html', data)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'main/blog_detail.html'
    context_object_name = 'blog_info'
    fields = ['text', 'image', 'video', 'date', 'category']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object.category
        context['category'] = category
        return context
    

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'main/create.html'
    form_class =BlogForm