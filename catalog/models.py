from django.db import models
from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта", blank=True, null=True)
    image = models.ImageField(upload_to="catalog/image", blank=True, null=True, verbose_name="Изображение")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Категория", related_name="products"
    )
    price = models.FloatField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    STATUS_CHOICES = [("awaiting_publication", "Ждет публикации"), ("publication", "Опубликовано")]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="awaiting_publication", verbose_name="Статус публикации"
    )
    owner = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL, verbose_name="Владелец")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
            ("can_delete_product", "Can delete product"),
        ]
