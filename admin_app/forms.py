from django import forms
from .models import *
from jsignature.forms import JSignatureField


class UserForm(forms.ModelForm):
    # READONLY_FIELDS = ('employee_name', 'date_of_service', 'medicaid_id', 'pa_name', 'employee_id', 'mobile_no')

    class Meta:
        model = Users
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by', 'is_active', 'is_admin', 'is_employee')
        fields = '__all__'
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter Member Name'}),
            'date_of_service': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'medicaid_id': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Medicaid Id'}),
            'pa_name': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Enter PA Name'}),
            'employee_id': forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter Employee ID'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter Mobile No'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '******'}),
        }

    # def __init__(self, readonly_form=False, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     if readonly_form:
    #         for field in self.READONLY_FIELDS:
    #             self.fields[field].widget.attrs['readonly'] = True
