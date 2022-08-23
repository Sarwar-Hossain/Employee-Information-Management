from django import forms
from .models import *
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget


# JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

class SignatureForm(forms.Form):
    signature = JSignatureField()


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by', 'email', 'password', 'is_active')
        fields = '__all__'
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter Member Name'}),
            'date_of_service': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'medicaid_id': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Medicaid Id'}),
            'pa_name': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Enter PA Name'}),
            'employee_id': forms.NumberInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Enter Employee ID'}),
            'mobile_no': forms.NumberInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Enter Mobile No'}),
        }


class DemographicsForm(forms.ModelForm):
    class Meta:
        model = Demographics
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Enter Your Last Name'}),
            'social_security_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your social security number'}),
            'street_address': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Enter Your Street address'}),
            'city_town': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Enter Your city/town'}),
            'state_zip_code': forms.NumberInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Enter state zip code'}),
            'home_phone': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter Your home phone number'}),
            'cell_phone': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter cell phone number'}),
        }


class DemoUserForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by', 'email', 'password', 'is_active')
        fields = '__all__'
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'User'}),
            'date_of_service': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'medicaid_id': forms.NumberInput(attrs={'class': 'form-control'})
        }


class HoursAvailableForm(forms.ModelForm):
    is_day = forms.BooleanField(required=False, initial=False)
    is_night = forms.BooleanField(required=False, initial=False)
    is_live_in = forms.BooleanField(required=False, initial=False)
    is_saturday = forms.BooleanField(required=False, initial=False)
    is_sunday = forms.BooleanField(required=False, initial=False)
    is_monday = forms.BooleanField(required=False, initial=False)
    is_tuesday = forms.BooleanField(required=False, initial=False)
    is_wednesday = forms.BooleanField(required=False, initial=False)
    is_thursday = forms.BooleanField(required=False, initial=False)
    is_friday = forms.BooleanField(required=False, initial=False)

    # is_day = forms.BooleanField()

    class Meta:
        model = HoursAvailable
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'high_school_name': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Enter high school name',
                                                       'required': 'required'}),
            'high_school_city_state': forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Enter City,State',
                                                             'required': 'required'}),
            'college': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Enter college', 'required': 'required'}),
            'college_city_state': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Enter City,State', 'required': 'required'}),
        }


class ProfessionalTrainingForm(forms.ModelForm):
    is_graduate: forms.BooleanField(required=False, initial=False)

    class Meta:
        model = ProfessionalTraining
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'name_of_school_city_state': forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter name of school, city,state'}),
            'entrance_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'certificate_degree': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Enter certificate / degree',
                                                         'required': 'required'}),
        }


class SkillsChecklistForm(forms.ModelForm):
    is_home_care = forms.BooleanField(required=False, initial=False)
    is_denture_care = forms.BooleanField(required=False, initial=False)
    is_non_sterile_dressing = forms.BooleanField(required=False, initial=False)
    is_orthopedics = forms.BooleanField(required=False, initial=False)
    is_special_diets = forms.BooleanField(required=False, initial=False)
    is_range_of_motion = forms.BooleanField(required=False, initial=False)
    is_vital_signs = forms.BooleanField(required=False, initial=False)
    is_diabetes_care = forms.BooleanField(required=False, initial=False)
    is_kosher_cooking = forms.BooleanField(required=False, initial=False)
    is_transfer_techniques = forms.BooleanField(required=False, initial=False)
    is_urine_testing = forms.BooleanField(required=False, initial=False)
    is_patient_teaching = forms.BooleanField(required=False, initial=False)
    is_household_maintenance = forms.BooleanField(required=False, initial=False)
    is_hoyer_lift = forms.BooleanField(required=False, initial=False)
    is_geriatrics = forms.BooleanField(required=False, initial=False)
    is_laundry = forms.BooleanField(required=False, initial=False)
    is_foyer_lift = forms.BooleanField(required=False, initial=False)
    is_child_care = forms.BooleanField(required=False, initial=False)
    is_bed_bath = forms.BooleanField(required=False, initial=False)
    is_ostomy_care = forms.BooleanField(required=False, initial=False)
    is_newborn_care = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = SkillsChecklist
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'other1': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Others'}),
            'other2': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Others'}),
            'other3': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Others'}),
        }


class TransportationForm(forms.ModelForm):
    is_bus_train_car = forms.BooleanField(required=False, initial=False)
    is_valid_licenses = forms.BooleanField(required=False, initial=False)
    is_permission_for_criminal_background = forms.BooleanField(required=False, initial=False)
    is_personal_assistant_guide = forms.BooleanField(required=False, initial=False)
    signature_img = JSignatureField()

    class Meta:
        model = Transportation
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'routes': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Type routes'}),
            'printed_name': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Type printed name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class AddProduct(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    product_mfg = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                  required=True)
    product_exp = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                                  required=True)
    department = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}), required=True)
