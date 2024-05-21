
from rest_framework import serializers
from shop.models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']

class CategorySerializer(serializers.ModelSerializer):
    # products = ProductSerializer(many=True)
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated', 'products']

    # def get_products(self, instance):
    #     queryset =