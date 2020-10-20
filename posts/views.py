from django.views.generic import ListView
from .models import Post


class PostsView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
