from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView
from django.urls import path

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="post_list"),
    path("blog/new/", BlogCreateView.as_view(), name="post_create"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("blog/update/<int:pk>/", BlogUpdateView.as_view(), name="post_update"),
    path("blog/delete/<int:pk>/", BlogDeleteView.as_view(), name="post_confirm_delete"),
]
