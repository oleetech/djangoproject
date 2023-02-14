from django import forms
from django.forms import formset_factory
from . models import Item

class ItemForm(forms.ModelForm):
    class Meta :
        model = Item
        fields = ['item_code','item_name','item_description','item_price','item_qty','item_picture']
        widgets = {
            'item_description':forms.TextInput()
        }

ItemFormSet = formset_factory(ItemForm,extra=1)

