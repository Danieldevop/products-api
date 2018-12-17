from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer

import pdb

@csrf_exempt
def products_view(request):

	if request.method == 'GET':
		product_query = Product.objects.all()
		response = ProductSerializer(product_query, many=True)
		return JsonResponse(response.data, safe=False)

	if request.method == 'POST':
		product_request = JSONParser().parse(request)
		product_serializer = ProductSerializer(data=product_request)

		if product_serializer.is_valid():
			product_serializer.save()

			return JsonResponse(product_serializer.data, status=201)
		
		return JsonResponse(product_serializer.errors, status=400)

@csrf_exempt
def detail_product_view(request, pk):
	#pdb.set_trace()
	try:
		detailed_product_query = Product.objects.get(pk=pk)
	except Product.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		response = ProductSerializer(detailed_product_query)
		return JsonResponse(response.data)

	if request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ProductSerializer(detailed_product_query, data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)

		return JsonResponse(serializer.errors, status=400)

	if request.method == 'DELETE':
		detailed_product_query.delete()
		return HttpResponse(status=201)


		




	