from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
	sku = models.UUIDField(default=uuid.uuid4(), editable=False)
	product_name = models.CharField(max_length=300, null=False)
	product_description = models.TextField()
	product_stock = models.IntegerField()
	product_price = models.IntegerField()
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return 'Model: {}, {}, {}, {}, {}, {}'.format(
			self.sku, 
			self.product_name, 
			self.product_description, 
			self.product_stock, 
			self.product_price, 
			self.created_date
		) 

	class Meta:
		ordering = ('created_date',)
