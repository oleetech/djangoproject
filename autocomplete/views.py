from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import City
# Create your views here.
def home(request):
  return render(request,'autocomplete/index.html')

def autocomplete(request):
    term = request.GET.get('term', '')
    suggestions = City.objects.filter(name__icontains=term).values_list('name', flat=True)
    return JsonResponse(list(suggestions), safe=False)