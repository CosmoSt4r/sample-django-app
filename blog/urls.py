from django.urls import path
from .views import BlogListView, BlogDetailView, CreatePostView


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_details'),
    path('post/new/', CreatePostView.as_view(), name='new_post')
]
