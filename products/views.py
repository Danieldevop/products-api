from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics

class products_view(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class detail_product_view(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
