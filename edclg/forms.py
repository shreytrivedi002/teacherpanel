from django import forms
from .models import pdfstore

class pdfupform(forms.ModelForm):
    class Meta:
        model = pdfstore
        fields = [
            'file',
            # 'unqid'
        
         ]



