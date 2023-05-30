from rest_framework.serializers import ModelSerializer
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class SubCategorySerializer(ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'name']


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class WarrantySerializer(ModelSerializer):
    class Meta:
        model = Warranty
        fields = ['id', 'name']


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "discount_price", "image"]
