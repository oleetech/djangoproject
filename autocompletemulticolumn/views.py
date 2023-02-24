from django.shortcuts import render
from django.http import JsonResponse
from .models import Autocomplete
# Create your views here.
def home(request):
 return render(request,'autocompletemulticolumn/index.html')

def autocomplete(request):
    term = request.GET.get('term')
    results = []
    if term:
        results = list(Autocomplete.objects.filter(name__icontains=term).values('name', 'category', 'description'))
    return JsonResponse(results, safe=False)