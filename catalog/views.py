from catalog.models import Product
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


def home(request):
    products = Product.objects.all()
    contex = {"products": products}
    return render(request, "base.html", context=contex)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо,{name}, ваше сообщение получено!")

    return render(request, "contacts.html")


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    contex = {"product": product}
    return render(request, "product_detail.html", context=contex)
