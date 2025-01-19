from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comments, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        search_query = self.request.GET.get('search', "")
        return Post.objects.filter(title__icontains=search_query) if search_query else Post.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        return context
    
   
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'home.html', {'cat_menu_list' : cat_menu_list})


def CategoryView(request, cats):
    # Handle category not found gracefully
    category_name = cats.replace('-', ' ').title()
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        return render(request, "blog/category_not_found.html", {'category': category_name})
    
    category_posts = Post.objects.filter(category=category)
    return render(request, "blog/categories.html", {'cats': category_name, 'category_post': category_posts})


class PostDetailsViews(DetailView):
    model = Post
    template_name = "post_details.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cat_menu'] = Category.objects.all()
        return context
    

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)

   
class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')    


def profile(request):
    user = request.user
    search_query = request.GET.get('search', '')

    posts = Post.objects.filter(author = user, title__icontains=search_query) if search_query else Post.objects.filter(author=user)
    
    
    return render(request, "profile.html", {'posts' : posts})

