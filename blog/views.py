from blog.models import Blog
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView


class BlogListView(ListView):
    model = Blog
    template_name = "blog/post_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(published=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "preview_image", "published"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/post_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "preview_image", "published"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.object.pk])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")
