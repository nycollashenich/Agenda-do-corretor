from django import forms
from .models import Imovel

class ImovelModelForm(forms.ModelForm):
    
    class Meta:
        model = Imovel
        fields = '__all__' 
        
         
