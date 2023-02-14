from django.db import models

# Create your models here.

class Item(models.Model):
  item_code = models.CharField(max_length=20)
  item_name = models.CharField(max_length=255)
  item_description = models.TextField()
  item_price = models.DecimalField(max_digits=10,decimal_places=2)
  item_qty = models.PositiveIntegerField()
  item_picture = models.ImageField(upload_to='items/')

  def __str__(self):
    return self.item_code


