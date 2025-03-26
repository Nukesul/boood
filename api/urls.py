from django.urls import path
from . import views

urlpatterns = [
    # Публичные маршруты
    path('api/public/branches/', views.PublicBranchList.as_view(), name='public-branch-list'),
    path('api/public/categories/', views.PublicCategoryList.as_view(), name='public-category-list'),
    path('api/public/products/', views.PublicProductList.as_view(), name='public-product-list'),

    # Админские маршруты
    path('api/admin/login/', views.AdminLoginView.as_view(), name='admin-login'),  
    path('api/admin/users/', views.UserList.as_view(), name='user-list'),
    path('api/admin/users/<int:pk>/', views.UserDelete.as_view(), name='user-delete'),
    path('api/admin/branches/', views.BranchListCreate.as_view(), name='branch-list-create'),
    path('api/admin/branches/<int:pk>/', views.BranchDetail.as_view(), name='branch-detail'),
    path('api/admin/categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
    path('api/admin/subcategories/', views.SubcategoryListCreate.as_view(), name='subcategory-list-create'),
    path('api/admin/subcategories/<int:pk>/', views.SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('api/admin/products/', views.ProductListCreate.as_view(), name='product-list-create'),
    path('api/admin/products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('api/admin/promo/', views.PromoCodeView.as_view(), name='promo-code'),

    # Маршруты для заказов
    path('api/orders/', views.OrderCreate.as_view(), name='order-create'),

    # Маршруты для авторизации
    path('api/auth/register/', views.RegisterView.as_view(), name='register'),
    path('api/auth/login/', views.LoginView.as_view(), name='login'),
]