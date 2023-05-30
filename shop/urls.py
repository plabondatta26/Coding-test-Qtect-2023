from django.urls import path
from .views import ProductView, ProductListAPIView, BrandListAPIView, CategoryListAPIView, SubCategoryListAPIView,\
    WarrantyListAPIView, SellerListAPIView

urlpatterns = [
    path('', ProductView.as_view()),
    path('api/product/list/', ProductListAPIView.as_view()),
    path('api/brand/list/', BrandListAPIView.as_view()),
    path('api/category/list/', CategoryListAPIView.as_view()),
    path('api/sub/category/list/', SubCategoryListAPIView.as_view()),
    path('api/warranty/list/', WarrantyListAPIView.as_view()),
    path('api/seller/list/', SellerListAPIView.as_view()),
]
