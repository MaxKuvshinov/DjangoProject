from django.views import View
from django.views.generic import ListView, DetailView

from catalog.models import Product
from django.http import HttpResponse
from django.shortcuts import render


class CatalogHomeView(ListView):
    model = Product
    template_name = 'catalog/base.html'
    context_object_name = 'products'


class CatalogContactsView(View):
    def get(self, request):
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо,{name}, ваше сообщение получено!")


class CatalogDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


