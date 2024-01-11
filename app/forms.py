from django import forms
from app.models import *

class DeptForms(forms.ModelForm):
    class Meta:
        model=Dept 
        fields='__all__'

class EmpForms(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'