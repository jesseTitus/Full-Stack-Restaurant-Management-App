# serializers.py
from rest_framework import serializers
from .models import Menu, MenuCategory
from decimal import Decimal

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MenuCategory
#         fields = ['id', 'name']

class MenuSerializer(serializers.ModelSerializer):
    info = serializers.CharField(source='description')#just renaming field
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = CategorySerializer()#relationship serializer
    class Meta:
        model = Menu
        fields = ['id', 'name', 'category', 'price', 'price_after_tax', 'info']  # Fields to include in the serialized output
        depth = 1

    def calculate_tax(self, product:Menu):
        return product.price * Decimal(1.1)