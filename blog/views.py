from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class BlogListView(ListView):

    model = Post
    context_object_name = 'posts_list'
    template_name = 'home.html'


class BlogDetailView(DetailView):

    model = Post
    context_object_name = 'post'
    template_name = 'post_details.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'
