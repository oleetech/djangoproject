from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NidForm,CitizenForm
from .models import Citizen,Nid

# Create your views here.
def home(request):
 return HttpResponse('Hello')

def citizen_list(request):
 citizens = Citizen.objects.all()
 return render(request,'nid/citizen_list.html',{'citizens':citizens})

def add_citizen(request):
 if request.method == 'POST':
   citizen_form = CitizenForm(request.POST)
   nid_form = NidForm(request.POST)
   if citizen_form.is_valid() and nid_form.is_valid():
     citizen = citizen_form.save() # return a id 
     nid = nid_form.save(commit=False)
     nid.citizen = citizen
     nid.save()
     return redirect('citizen_list')
   else:
    return HttpResponse('Please Fill Form Correctly')


 else:
   citizen_form = CitizenForm()
   nid_form = NidForm()
   context = {
    'citizen_form':citizen_form,
    'nid_form':nid_form
   }
   return render(request,'nid/add_citizen.html',context)

def update_citizen(request,id):
 cityzen = Citizen.objects.get(id=id)
 nid = Nid.objects.get(id=id)
 if request.method == 'POST':
  citizen_form = CitizenForm(request.POST,instance = cityzen)
  nid_form = NidForm(request.POST,instance = nid)
  if citizen_form.is_valid() and nid_form.is_valid():
    cityzen=  citizen_form.save()
    nids = nid_form.save(commit=False)
    nids.cityzen = cityzen 
    nids.save()
    return redirect('citizen_list')
  else:
    return HttpResponse('Please Fill Form Correctly')

   
 else:
   citizen_form = CitizenForm(instance=cityzen)
   nid_form = NidForm(instance=nid)
   context = {
    'citizen_form':citizen_form,
    'nid_form':nid_form
   }
   return render(request,'nid/add_citizen.html',context)

def delete_citizen(request,id):
 Citizen.objects.filter(id=id).delete()
 Nid.objects.filter(id=id).delete()
 return redirect('citizen_list')
  


def search_nid(request):
 if request.method == "GET":
    query = request.GET.get('nid_number')
    if query:
        nid = Nid.objects.filter(nid_number=query)

        
    else:
        nid = None
    context = {'nids': nid} 
   
    return render(request,'nid/search.html',context)

def search_citizen(request):
    if request.method == 'POST':
        nid_number = request.POST['nid_number']
        try:
            nid = Nid.objects.get(nid_number=nid_number)
            citizen = nid.citizen
        except Nid.DoesNotExist:
            citizen = None
        return render(request, 'nid/search.html', {'citizen': citizen})
    else:
          
      return render(request, 'nid/citizen_list.html')   
