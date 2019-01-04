from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	
	path('products', views.products_view.as_view()),
	path('products/<int:pk>', views.detail_product_view.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)