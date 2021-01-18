from django import forms
from .models import Reserve , Property


class ReserveForm(forms.ModelForm):
    class Meta : 
        model = Reserve
        fields = '__all__'

        def clean(self):
         fields = self.cleaned_data['name','email','notes']
     
        
