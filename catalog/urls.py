from catalog.apps import CatalogConfig
from catalog.views import contacts, home
from django.urls import path

app_name = CatalogConfig.name

urlpatterns = [path("", home, name="home"), path("contacts/", contacts, name="contacts")]
