from rest_framework import serializers
from .models import Branch, Category, Subcategory, Product, Order
from django.contrib.auth.models import User

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'address']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'emoji', 'has_multiple_prices']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Вложенный сериализатор для категории
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )  # Для записи через API

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category', 'category_id']

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(read_only=True)  # Вложенный сериализатор для подкатегории
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(), source='subcategory', write_only=True
    )  # Для записи через API
    branch = BranchSerializer(read_only=True)  # Вложенный сериализатор для филиала
    branch_id = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), source='branch', write_only=True
    )  # Для записи через API

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'price', 'small_price', 'medium_price', 'large_price',
            'subcategory', 'subcategory_id', 'branch', 'branch_id', 'image'
        ]

    def validate(self, data):
        """
        Проверка: если категория имеет has_multiple_prices=True, price должен быть None,
        иначе small_price, medium_price, large_price должны быть None.
        """
        subcategory = data.get('subcategory')
        if subcategory and subcategory.category.has_multiple_prices:
            if data.get('price') is not None:
                raise serializers.ValidationError(
                    "Для категорий с множественными ценами поле 'price' должно быть пустым."
                )
        else:
            if any(data.get(field) is not None for field in ['small_price', 'medium_price', 'large_price']):
                raise serializers.ValidationError(
                    "Для категорий с одной ценой поля 'small_price', 'medium_price', 'large_price' должны быть пустыми."
                )
        return data

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Вложенный сериализатор для продуктов
    product_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), many=True, source='products', write_only=True
    )  # Для записи через API

    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'product_ids', 'total', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PromoCodeSerializer(serializers.Serializer):
    promoCode = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=150)