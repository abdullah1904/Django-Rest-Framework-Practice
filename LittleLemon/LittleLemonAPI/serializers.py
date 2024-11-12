from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField('calculate_tax')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price','stock','price_after_tax','category', 'category_id']
        extra_kwargs = {
            'price': {'min_value': 2},
            'stock':{'source': 'inventory','min_value':0}
        }
    def calculate_tax(self,item:MenuItem):
        return item.price * Decimal(1.1)
