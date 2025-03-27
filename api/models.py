from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название филиала")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    
    def __str__(self):
        return f"{self.name} ({self.address})"

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    emoji = models.CharField(max_length=10, blank=True, null=True, verbose_name="Эмодзи")
    
    def __str__(self):
        return f"{self.emoji} {self.name}" if self.emoji else self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Subcategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название подкатегории")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена")
    prices = models.JSONField(null=True, blank=True, verbose_name="Цены (для пиццы)")  # Для пиццы с разными размерами
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name="Подкатегория")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Филиал")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итого")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"Заказ #{self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"