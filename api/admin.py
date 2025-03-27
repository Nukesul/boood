from django.contrib import admin
from django import forms
from .models import Branch, Category, Subcategory, Product, Order

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.subcategory:
            category = self.instance.subcategory.category
            if category.has_multiple_prices:
                # Если категория поддерживает множественные цены (например, пицца), скрываем price
                self.fields['price'].widget = forms.HiddenInput()
            else:
                # Если нет, скрываем small, medium, large
                self.fields['small_price'].widget = forms.HiddenInput()
                self.fields['medium_price'].widget = forms.HiddenInput()
                self.fields['large_price'].widget = forms.HiddenInput()

        # Динамическое обновление полей при выборе подкатегории
        if 'subcategory' in self.data:
            try:
                subcategory_id = int(self.data.get('subcategory'))
                subcategory = Subcategory.objects.get(id=subcategory_id)
                if subcategory.category.has_multiple_prices:
                    self.fields['price'].widget = forms.HiddenInput()
                else:
                    self.fields['small_price'].widget = forms.HiddenInput()
                    self.fields['medium_price'].widget = forms.HiddenInput()
                    self.fields['large_price'].widget = forms.HiddenInput()
            except (ValueError, Subcategory.DoesNotExist):
                pass

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'emoji', 'has_multiple_prices')
    search_fields = ('name',)

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name', 'get_price_display', 'subcategory', 'branch', 'image')
    list_filter = ('subcategory', 'branch')
    search_fields = ('name',)

    def get_price_display(self, obj):
        if obj.subcategory and obj.subcategory.category.has_multiple_prices:
            prices = []
            if obj.small_price:
                prices.append(f"Маленькая: {obj.small_price}")
            if obj.medium_price:
                prices.append(f"Средняя: {obj.medium_price}")
            if obj.large_price:
                prices.append(f"Большая: {obj.large_price}")
            return ", ".join(prices) or "Не указаны"
        return obj.price or "Не указана"
    get_price_display.short_description = "Цена"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('user__username',)
    filter_horizontal = ('products',)