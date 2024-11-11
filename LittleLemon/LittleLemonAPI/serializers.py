from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title','slug']
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField('calculate_tax')
    category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price','stock','price_after_tax','category']
    def calculate_tax(self,item:MenuItem):
        return item.price * Decimal(1.1)
