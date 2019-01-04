from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product
from .serializers import ProductSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


import pdb

@api_view(['GET', 'POST'])
def products_view(request, format=None):

	if request.method == 'GET':
		product_query = Product.objects.all()
		response = ProductSerializer(product_query, many=True)
		return Response(response.data)

	if request.method == 'POST':
		product_serializer = ProductSerializer(data=request.data)

		if product_serializer.is_valid():
			product_serializer.save()
			return Response(product_serializer.data, status=status.HTTP_201_CREATED)
		
		return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_product_view(request, pk, format=None):
	#pdb.set_trace()
	try:
		detailed_product_query = Product.objects.get(pk=pk)
	except Product.DoesNotExist:
		return Response(status=status.HTTP_400_NOT_FOUND)

	if request.method == 'GET':
		response = ProductSerializer(detailed_product_query)
		return Response(response.data)

	if request.method == 'PUT':
		serializer = ProductSerializer(detailed_product_query, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	if request.method == 'DELETE':
		detailed_product_query.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


		




	