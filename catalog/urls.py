from catalog.apps import CatalogConfig
from catalog.views import CatalogContactsView, CatalogDetailView, CatalogHomeView
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product_detail/<int:product_id>/", CatalogDetailView.as_view(), name="product_detail"),
]
