from django.shortcuts import render
from .models import Post, Category
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    posts = Post.objects.all
    categories = Category.objects.all()
    context = {'posts': posts, 'categories': categories}
    return render(request, 'blog/index.html', context)


def by_category(request, category_id):
    posts = Post.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'posts': posts, 'categories': categories, 'current_categories': current_category}
    return render(request, 'blog/by_category.html', context)


class PostCreateView(CreateView):
    template_name = 'blog/create.html'
    form_class = PostForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
