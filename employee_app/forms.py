from django import forms
from jsignature.forms import JSignatureField
from .models import *


# class EmployeeForm(forms.Form):
#     employee_name = forms.CharField(max_length=50, help_text='Type Employee Name:',
#                                     widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                   'placeholder': 'User'})
#                                     )
#     medicaid_id = forms.IntegerField()
#     date_of_service = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     pa_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
#                                                                            'placeholder': 'User'}))
#     employee_id = forms.IntegerField()
#     mobile_no = forms.CharField(max_length=15)
#     is_active = forms.BooleanField(required=False)
#     password = forms.TextInput()
#     email = forms.EmailField(max_length=30)
#     signature = JSignatureField()


class SignatureForm(forms.Form):
    signature = JSignatureField()


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = DemoUser
        # exclude = ('created_by', 'created_at', 'updated_at', 'updated_by', 'email', 'password', 'is_active')
        fields = '__all__'
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'User'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }


class DemoUserForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by', 'email', 'password', 'is_active')
        fields = '__all__'
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'User'}),
            'date_of_service': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }


class AddProduct(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    product_mfg = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                  required=True)
    product_exp = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                  required=True)
    department = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}), required=True)
