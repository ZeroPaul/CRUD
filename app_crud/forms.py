from django import forms
from app_crud.models import Producto

class ProductoForm(forms.ModelForm):
     class Meta:
         model = Producto
