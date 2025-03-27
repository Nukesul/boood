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
        fields = ['id', 'name', 'emoji']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(read_only=True)
    branch = BranchSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'prices', 'subcategory', 'branch', 'image']

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PromoCodeSerializer(serializers.Serializer):
    promoCode = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=150)