from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .services import get_product_from_cache, get_product_by_category


class CatalogHomeView(ListView):
    model = Product
    template_name = "catalog/base.html"
    context_object_name = "products"

    def get_queryset(self):
        return get_product_from_cache()


class CatalogContactsView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо,{name}, ваше сообщение получено!")


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_create.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.can_unpublish_product"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied("Нет прав для редактирования продукта")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if self.request.user != product.owner and not self.request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("Нет прав для редактирования продукта")
        return product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:home")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if self.request.user != product.owner and not self.request.user.has_perm("can_delete_product"):
            raise PermissionDenied("Нет прав для удаления продукта")
        return product

    def handle_no_permission(self):
        return redirect("catalog:category_list")


class ProductByCategoryView(View):
    model = Category

    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        products = get_product_by_category(pk)
        return render(request, "catalog/category_products.html", {"category": category, "products": products})


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category_list.html"
    context_object_name = "categories"
