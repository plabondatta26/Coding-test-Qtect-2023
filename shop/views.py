import operator
from functools import reduce

from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from rest_framework.generics import ListAPIView
from .serializers import *

from .models import Category, Brand, Warranty, Product


# Create your views here.
class ProductView(generic.TemplateView):
    template_name = 'index.html'


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        min_price = self.request.query_params.get('min_price', None)
        max_price = self.request.query_params.get('max_price', None)
        category = self.request.query_params.getlist('category[]', None)
        sub_category = self.request.query_params.getlist('sub_category[]', None)
        brand = self.request.query_params.getlist('brand[]', None)
        warranty = self.request.query_params.getlist('warranty[]', None)
        seller = self.request.query_params.getlist('seller[]', None)
        filter_data = dict()
        if category:
            filter_data["category_id__in"] = category
        if sub_category:
            filter_data["sub_category_id__in"] = sub_category
        if brand:
            filter_data["brand_id__in"] = brand
        if warranty:
            filter_data["warranty_id__in"] = warranty
        if seller:
            filter_data["seller_id__in"] = seller

        if min_price and max_price:
            self.queryset = self.queryset.filter(Q(price__range=[min_price, max_price]) |
                                                 Q(discount_price__range=[min_price, max_price]))
        elif filter_data:
            self.queryset = self.queryset.filter(reduce(operator.or_,
                                                        (Q(**d) for d in (dict([i]) for i in filter_data.items()))))
        return self.queryset.distinct()


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return self.queryset.all().distinct()


class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        return self.queryset.all().distinct()


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_queryset(self):
        return self.queryset.all().distinct()


class WarrantyListAPIView(ListAPIView):
    queryset = Warranty.objects.all()
    serializer_class = WarrantySerializer

    def get_queryset(self):
        return self.queryset.all().distinct()


class SellerListAPIView(ListAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

    def get_queryset(self):
        return self.queryset.all().distinct()
