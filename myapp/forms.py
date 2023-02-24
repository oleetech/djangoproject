from django import forms
from .models import OrderInfo,OrderItem

class OrderInfoForm(forms.ModelForm):
    class Meta:
      model = OrderInfo
      fields = ('customer_name','address')

class OrderItemForm (forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model =  OrderItem    
        fields = ('product_name','quantity','price')
        exclude = ('id',)
