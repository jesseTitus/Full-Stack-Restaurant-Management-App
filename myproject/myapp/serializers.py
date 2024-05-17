# serializers.py
from rest_framework import serializers
from .models import Menu, MenuCategory, Booking
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    info = serializers.CharField(source='description')#just renaming field
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = CategorySerializer(read_only=True)#relationship serializer
    category = serializers.HyperlinkedRelatedField(
        queryset = MenuCategory.objects.all(),
        view_name='category-detail'
    )
    class Meta:
        model = Menu
        fields = ['id', 'name', 'category', 'price', 'price_after_tax', 'info']  # Fields to include in the serialized output
        # depth = 1   #instead of categorSerialzer, reduces api calls

    def calculate_tax(self, product:Menu):
        return product.price * Decimal(1.1)