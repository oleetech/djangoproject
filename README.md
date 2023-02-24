# One to Many Relationship Practical (Sales Page Crud)

## Screenshots

![App Screenshot]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://i.postimg.cc/N02K6GXS/create.png))
![App Screenshot]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://i.postimg.cc/CLdSBPk6/list.png)
![App Screenshot]([https://via.placeholder.com/468x300?text=App+Screenshot+Here](https://i.postimg.cc/4xNLNqcm/edit-update.png)
## create App myapp
```bash
python manage.py startapp myapp
```
## linking with DjangoProject
### settings.py
```python
INSTALLED_APPS = [
    'myapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
### urls.py (Django Project)
```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',include('myapp.urls')),
]
```
### Create urls.py (myapp)
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
]

### views.py
```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
 return HttpResponse('Hello')
```
## Start One to Many Relationship Practical Journey

### models.py
```python
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
```
### forms.py
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

### urls.py (myapp)
```python
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.order_create,name='order_create'),
    path('order_list/',views.order_list,name='order_list'),
    path('order_update/<int:id>',views.order_update,name='order_update'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),
]
```
### views.py
```python
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
```

### Templates
***templates/myapp/create.html***
```html
    <h1>Order Info</h1>
    <form  method="post">
        {% csrf_token %}
        {{ order_info_form.as_p}}

        <table>
            <thead>
              <tr>
                <th>Product</th>
                <th>Quantity</th>
                <th>Price</th>
              </tr>
            </thead>
            <tbody>
                {{ order_item_formset.management_form  }}
                {% for form in order_item_formset  %}
                <tr>
                    <td>{{ form.product_name }}</td>
                    <td>{{ form.quantity }}</td>
                    <td>{{ form.price }}</td>
                    <td>{{ form.id }}</td>
                 

                </tr>
                {% endfor %}

            </tbody>
        </table>
        <button type="submit">Save</button>
    </form>
    ```
***templates/myapp/order_list.html***
```html
<h1>Order List</h1>
  <a href="{% url 'order_create' %}">Create New Order</a>
  <table>
    <thead>
      <tr>
        <th>Customer Name</th>
        <th>Address</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      {% for order in orders %}
        <tr>
          
          <td>{{ order.customer_name }}</td>
          <td>{{ order.address }}</td>
          <td>
            <a href="{% url 'order_update' order.id %}">Edit</a>
            <a href="{% url 'order_delete' order.id %}">Delete</a>
          </td>
        </tr>
      {% empty %}
        <tr>
          <td colspan="4">No orders found.</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
  ```

