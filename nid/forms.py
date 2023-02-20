from django import forms
from .models import Citizen,Nid

class CitizenForm(forms.ModelForm):
    class Meta:
      model = Citizen
      fields = ['name','date_of_birth','address']
class NidForm (forms.ModelForm):
  class Meta:
    model = Nid
    fields = ['nid_number','issue_date','expire_date']     
    
     