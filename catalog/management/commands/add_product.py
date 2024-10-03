from catalog.models import Category, Product
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "add product to the databse"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "catalog_fixture.json")
        self.stdout.write(self.style.SUCCESS("Данные загружены"))
