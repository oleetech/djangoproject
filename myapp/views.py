from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse

from .models import OrderInfo,OrderItem
from .forms import OrderInfoForm,OrderItemForm
from django.forms import modelformset_factory
# Create your views here.
def home(request):
 return HttpResponse('Hello')

def order_create(request):
 OrderItemFormset =  modelformset_factory(OrderItem,form=OrderItemForm,extra=2)
 if request.method == "POST":
   order_info_form = OrderInfoForm(request.POST)
   order_item_formset = OrderItemFormset(request.POST,queryset=OrderItem.objects.none())
   if order_info_form.is_valid() and order_item_formset.is_valid():
     order_info = order_info_form.save()
     order_items = order_item_formset.save(commit=False)
     for order_item in order_items:
        order_item.order = order_info
        order_item.save()
     return HttpResponse('save')    
   else:
     return HttpResponse('not Valid')  
 else:
   order_info_form = OrderInfoForm()
   order_item_formset = OrderItemFormset(queryset=OrderItem.objects.none())
   context = {'order_info_form':order_info_form,'order_item_formset':order_item_formset}
   return render(request,'myapp/create.html',context )


def order_list(request):
    orders = OrderInfo.objects.all()
    return render(request, 'myapp/order_list.html', {'orders': orders})


def order_update(request, id):
  order_info = get_object_or_404(OrderInfo,id=id)
  OrderItemFormset = modelformset_factory(OrderItem,form=OrderItemForm,extra=0)
  if request.method == 'POST':
    order_info_form = OrderInfoForm(request.POST,instance=order_info)
    order_item_formset = OrderItemFormset(request.POST,queryset=order_info.order_item.all())
    if order_info_form.is_valid() and order_item_formset.is_valid():
      order_info = order_info_form.save()
      order_items = order_item_formset.save(commit=False)
      for order_item in order_items:
        order_item.order = order_info
        order_item.save()
      return HttpResponse('save')   
       

  else:
    order_info_form = OrderInfoForm(instance=order_info)
    order_item_formset = OrderItemFormset(queryset=order_info.order_item.all())
  return render(request,'myapp/create.html',{'order_info_form':order_info_form,'order_item_formset':order_item_formset})

def order_delete(request, id):
    order = get_object_or_404(OrderInfo, id=id)
    order.delete()
    return redirect('order_list')