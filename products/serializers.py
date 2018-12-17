from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('sku', 'product_name', 'product_description', 'product_stock', 'product_price', 'created_date')
	