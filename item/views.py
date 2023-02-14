from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ItemForm,ItemFormSet
from . models import Item



# Create your views here.


def item_create(request):
    if request.method == 'POST' :

        formset = ItemFormSet(request.POST,request.FILES,prefix = 'item',)
        if formset.is_valid():
              
            for form in formset :
                instance = form.save(commit=False)
                instance.save()
                # if form.cleaned_data.get('item_price') is None:
                #    return render(request,'item/item_formset.html',{'formset':formset})
                # else:
                       
                #     form.save()
            return redirect('item_list')
    else :
        formset = ItemFormSet(prefix='item')  
    return render(request,'item/item_formset.html',{'formset':formset})

def item_list(request):
 items = Item.objects.all()
 return render (request,'item/item_list.html',{'items':items})

def item_update(request,id):
 item = Item.objects.get(id=id) 
 if request.method == 'POST':

   form = ItemForm(request.POST, instance=item)
   if form.is_valid():
    
    form.save()
   return redirect('item_list')

 else:
    form = ItemForm(instance=item)
 return render(request,'item/item_form.html',{'form':form})


def item_delete(request,id):
 item = Item.objects.get(id=id) 
 item.delete()
 return redirect('item_list')   
