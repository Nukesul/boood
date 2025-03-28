from rest_framework import serializers
from .models import Branch, Category, Subcategory, Product, Order, User

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'address']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'emoji', 'has_multiple_prices']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer(read_only=True)
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    image = serializers.ImageField(use_url=True, allow_null=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'small_price', 'medium_price', 'large_price', 'subcategory', 'branch', 'image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'products', 'total', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']