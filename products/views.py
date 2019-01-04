from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


import pdb

class products_view(APIView):

	def get(self, request, format=None):
		product_query = Product.objects.all()
		response = ProductSerializer(product_query, many=True)
		return Response(response.data)

	def post(self, request, format=None):
		product_serializer = ProductSerializer(data=request.data)

		if product_serializer.is_valid():
			product_serializer.save()
			return Response(product_serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class detail_product_view(APIView):
	#pdb.set_trace()

	def get_product(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		product = self.get_product(pk)
		response = ProductSerializer(product)
		return Response(response.data)

	def put(self, request, pk, format=None):
		product = self.get_product(pk)
		serializer = ProductSerializer(product, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		product = self.get_product(pk)
		product.delete()
		response = {
			'Message': 'Deleted',
		}
		return Response(response)


		




	