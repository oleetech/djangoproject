# One to Many Relationship Practical (Sales Page Crud)

## create App myapp
```bash
python manage.py startapp myapp
```
##linking with DjangoProject
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

