from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    customer_name = models.CharField(max_length=255)
    address       = models.CharField(max_length=255)
    created_at    = models.DateField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE,related_name='order_item') 
    product_name = models.CharField(max_length=255)   
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)



'''
we have defined two models - OrderInfo and OrderItem. The OrderItem model has a foreign key relationship with the OrderInfo model.
'''    