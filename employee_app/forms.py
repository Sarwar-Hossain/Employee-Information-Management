from django import forms
from admin_app.models import Users
from .models import *
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget


# JSignatureField(widget=JSignatureWidget(jsignature_attrs={'color': '#CCC'}))

class SignatureForm(forms.Form):
    signature = JSignatureField()


class EmployeeForm(forms.ModelForm):
    READONLY_FIELDS = ('employee_name', 'date_of_service', 'medicaid_id', 'pa_name', 'employee_id', 'mobile_no')

    class Meta:
        model = Employee
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
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
        }

    def __init__(self, readonly_form=False, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        if readonly_form:
            for field in self.READONLY_FIELDS:
                self.fields[field].widget.attrs['readonly'] = True


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
    # is_graduate: forms.BooleanField(initial=False)
    CHOICES = [('True', 'Yes'),
               ('False', 'No')]
    is_graduate = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)

    class Meta:
        model = ProfessionalTraining
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'name_of_school_city_state': forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter name of school, city,state'}),
            'entrance_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'certificate_degree': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Enter certificate / degree'}),
        }


class SkillsChecklistForm(forms.ModelForm):
    is_home_care = forms.BooleanField(required=False, initial=True)
    is_denture_care = forms.BooleanField(required=False, initial=False)
    is_non_sterile_dressing = forms.BooleanField(required=False, initial=False)
    is_orthopedics = forms.BooleanField(required=False, initial=False)
    is_special_diets = forms.BooleanField(required=False, initial=True)
    is_range_of_motion = forms.BooleanField(required=False, initial=False)
    is_vital_signs = forms.BooleanField(required=False, initial=False)
    is_diabetes_care = forms.BooleanField(required=False, initial=False)
    is_kosher_cooking = forms.BooleanField(required=False, initial=False)
    is_transfer_techniques = forms.BooleanField(required=False, initial=False)
    is_urine_testing = forms.BooleanField(required=False, initial=False)
    is_patient_teaching = forms.BooleanField(required=False, initial=False)
    is_household_maintenance = forms.BooleanField(required=False, initial=True)
    is_hoyer_lift = forms.BooleanField(required=False, initial=False)
    is_geriatrics = forms.BooleanField(required=False, initial=False)
    is_laundry = forms.BooleanField(required=False, initial=True)
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


# Complete till TransportationForm
class TransportationForm(forms.ModelForm):
    CHOICES = [('True', 'Yes'),
               ('False', 'No')]
    is_bus_train_car = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_valid_licenses = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_permission_for_criminal_background = forms.ChoiceField(choices=CHOICES, initial=True, widget=forms.RadioSelect)
    is_personal_assistant_guide = forms.ChoiceField(choices=CHOICES, initial=True, widget=forms.RadioSelect)
    # is_bus_train_car = forms.BooleanField(required=False, initial=False)
    # is_valid_licenses = forms.BooleanField(required=False, initial=False)
    # is_permission_for_criminal_background = forms.BooleanField(required=False, initial=False)
    # is_personal_assistant_guide = forms.BooleanField(required=False, initial=False)
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


class EmployeeWithholdingCertificateForm(forms.ModelForm):
    CHOICES = [('True', 'Yes'),
               ('False', 'No')]
    is_single_or_married = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_married_jointly = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_head_of_household = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_two_jobs_total = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)

    # is_single_or_married = forms.BooleanField(required=False, initial=False)
    # is_married_jointly = forms.BooleanField(required=False, initial=False)
    # is_head_of_household = forms.BooleanField(required=False, initial=False)
    # is_two_jobs_total = forms.BooleanField(required=False, initial=False)

    employee_signature_img = JSignatureField()

    class Meta:
        model = EmployeeWithholdingCertificate
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'first_middle_name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Enter First name and middle initial'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                'placeholder': 'Enter Last name'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Enter your Address'}),
            'city_town_state_zip': forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter your City or Town, State, Zip Code'}),
            'employer_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Employer Name'}),
            'employer_address': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                       'placeholder': 'Employer Address'}),

            'social_security_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your social security number', 'readonly': True}),
            'children_under_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'others_dependents': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'other_income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'deductions': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'extra_withholding': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '$'}),
            'employer_identification_no': forms.NumberInput(
                attrs={'class': 'form-control', 'readonly': True,
                       'placeholder': 'Employment identification number (EIN)'}),

            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'first_date_of_employment': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class EmployeeWithholdingAllowanceCertificateForm(forms.ModelForm):
    CHOICES = [('True', 'Yes'),
               ('False', 'No')]
    is_new_york_resident = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_yonkers_resident = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_health_insurance = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)

    is_single_or_head_of_household = forms.BooleanField(required=False, initial=False)
    is_married = forms.BooleanField(required=False, initial=False)
    is_married_higher_single_rate = forms.BooleanField(required=False, initial=False)
    # is_new_york_resident = forms.BooleanField(required=False, initial=False)
    # is_yonkers_resident = forms.BooleanField(required=False, initial=False)
    is_exemption_allowances = forms.BooleanField(required=False, initial=False)
    is_new_hire = forms.BooleanField(required=False, initial=False)
    # is_health_insurance = forms.BooleanField(required=False, initial=False)

    employee_signature_img = JSignatureField()

    class Meta:
        model = EmployeeWithholdingAllowanceCertificate
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'first_middle_name': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'First Name and Middle Name Initial'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                'placeholder': 'Last Name'}),
            'permanent_home_address': forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Permanent Home Address (number and street '
                                                                            'or rural route )'}),
            'city_village_post_office': forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'City, Village or Post Office'}),
            'state': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'State'}),
            'employer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'employer_address': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'readonly': True}),
            'social_security_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Social Security Number', 'readonly': True}),
            'apartment_no': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Apartment Number'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Zip Code', 'readonly': True}),
            'total_newyork_yonkers_allowance': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_newyork_allowance': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_york_state_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'employer_identification_no': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'yonkers_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_york_city_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'employee_performed_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'employee_qualifies_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class EmployeeInformationAttestationForm(forms.ModelForm):
    is_citizen_us = forms.BooleanField(required=False, initial=False)
    is_non_citizen_us = forms.BooleanField(required=False, initial=False)
    is_lawful_resident = forms.BooleanField(required=False, initial=False)
    is_alien_authorize_to_work = forms.BooleanField(required=False, initial=False)

    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = EmployeeInformationAttestation
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employee_email_address': forms.EmailInput(attrs={'class': 'form-control',
                                                              'placeholder': 'example@gmail.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                'placeholder': 'Last Name'}),
            'other_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Other Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Address'}),
            'city_town': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Employer City, Town'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                            'placeholder': 'State'}),
            'employee_tp_no': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Employee Telephone No'}),
            'authorize_to_work': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Authorize to Work'}),
            'country_of_issuance': forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Country of Issuance'}),
            'apt_no': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Type Social Security Number', 'readonly': True, }),
            'apartment_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Apt. Number'}),
            'zip_code': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Type Zip Code', 'readonly': True, }),
            'ss_no_1': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_2': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_3': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_4': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_5': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_6': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_7': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_8': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'ss_no_9': forms.NumberInput(
                attrs={'class': 'form-control ap-otp-input', 'type': 'tel', 'maxlength': 1, 'data-index': 0}),
            'alien_reg_no': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Alien Registration Number/USCIS Number'}),
            'admission_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Admission No'}),
            'uscis_no': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Alien Registration Number /USCIS Number'}),
            'foreign_passport_no': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Foreign Passport No'}),
            # 'qr_code': forms.NumberInput(
            #     attrs={'class': 'form-control', 'placeholder': 'QR Code'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'today_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expire_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class TranslatorCertificateForm(forms.ModelForm):
    is_use_translator = forms.BooleanField(required=False, initial=False, disabled=True)
    is_preparer_assisted = forms.BooleanField(required=False, initial=False, disabled=True)

    preparer_signature_img = JSignatureField(required=False)

    class Meta:
        model = TranslatorCertificate
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                 'placeholder': 'Type First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                'placeholder': 'Type Last Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                              'placeholder': 'Address'}),
            'city_town': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                'placeholder': 'City or Town'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                            'placeholder': 'Type State'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True, }),
            'translator_today_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'readonly': True, }),
        }


class EmployerReviewVerificationForm(forms.ModelForm):
    class Meta:
        model = EmployerReviewVerification
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                 'placeholder': 'Type First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                'placeholder': 'Type Last Name'}),
            'middle_initial': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                     'placeholder': 'Middle Initial'}),
            'citizenship_status': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Citizenship Status'}),
            'document_title_list_a_1': forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Document Title'}),
            'issuing_authority_list_a_1': forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Issuing Authority'}),
            'document_no_e_list_a_1': forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Document No'}),
            'document_title_list_a_2': forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Document Title'}),
            'issuing_authority_list_a_2': forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Issuing Authority'}),
            'document_no_e_list_a_2': forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Document No'}),
            'document_title_list_a_3': forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Document Title'}),
            'issuing_authority_list_a_3': forms.TextInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Issuing Authority'}),
            'document_no_e_list_a_3': forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Document No'}),
            'document_title_list_b': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Document Title'}),
            'issuing_authority_list_b': forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Issuing Authority'}),
            'document_no_e_list_b': forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Document No'}),
            'document_title_list_c': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Document Title'}),
            'issuing_authority_list_c': forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Issuing Authority'}),
            'document_no_e_list_c': forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Document No'}),
            'additional_info_b_n_c': forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Enter Text'}),
            # 'qr_code': forms.TextInput(attrs={'class': 'form-control',
            #                                   'placeholder': 'Type State'}),

            'expire_date_e_list_a_1': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expire_date_e_list_a_2': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expire_date_e_list_a_3': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expire_date_e_list_b': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expire_date_e_list_c': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class EmploymentFirstDayForm(forms.ModelForm):
    first_day_employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = EmploymentFirstDay
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employer_title': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Employee Title'}),
            'employer_first_name': forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Employee First Name'}),
            'employer_last_name': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Employee Last Name'}),
            'business_organization_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                                 'placeholder': 'Business Organization Name'}),
            'business_organization_address': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                                    'placeholder': 'Business Organization Address'}),
            'city_town': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                'placeholder': 'City, Town'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                            'placeholder': 'State'}),
            'zip_code': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Zip Code', 'readonly': True, }),
            'today_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'employee_first_day': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class ReverificationRehiresForm(forms.ModelForm):
    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = ReverificationRehires
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Last Name'}),
            'document_title': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Document Title'}),
            'document_no': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Document Number'}),
            'employer_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Employer Name'}),
            'date_of_rehire': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expire_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reh_today_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'today_s_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class AcknowledgementOfReceiptForm(forms.ModelForm):
    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = AcknowledgementOfReceipt
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employee_printed_name': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Printed Name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class VoluntaryIdentificationForm(forms.ModelForm):
    CHOICES = [('True', 'Yes'),
               ('False', 'No')]

    is_male = forms.BooleanField(required=False, initial=False)
    is_female = forms.BooleanField(required=False, initial=False)
    is_disclose_sex = forms.BooleanField(required=False, initial=False)
    is_hispanic_or_latino = forms.ChoiceField(choices=CHOICES, initial=False, widget=forms.RadioSelect)
    is_middle_or_north_east = forms.BooleanField(required=False, initial=False)
    is_black_or_african_American = forms.BooleanField(required=False, initial=False)
    is_other_pacific_island = forms.BooleanField(required=False, initial=False)
    is_asian = forms.BooleanField(required=False, initial=False)
    is_american_indian_or_alaskan = forms.BooleanField(required=False, initial=False)
    is_two_or_more_races = forms.BooleanField(required=False, initial=False)
    is_disclose_info = forms.BooleanField(required=False, initial=False)
    is_disabled_veteran = forms.BooleanField(required=False, initial=False)

    is_recently_separated = forms.BooleanField(required=False, initial=False)
    is_armed_forces = forms.BooleanField(required=False, initial=False)
    is_other_protected_veteran = forms.BooleanField(required=False, initial=False)
    is_disclose_military_status = forms.BooleanField(required=False, initial=False)
    is_no_military_status = forms.BooleanField(required=False, initial=False)
    is_have_disability = forms.BooleanField(required=False, initial=False)
    is_no_disability = forms.BooleanField(required=False, initial=False)
    is_disclose_disability = forms.BooleanField(required=False, initial=False)

    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = VoluntaryIdentification
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'First Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Last Name'}),
            'business_unit_location': forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Business Unit Location'}),
            'department': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Department'}),
            'job_title_position': forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Job Title Position'}),
            'nature_of_disability': forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Nature of Disability'}),
            'voluntarily_info': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Voluntarily Info'}),

            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_of_active_duty': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'military_discharge_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'sign_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class AuthorizationBackgroundCheckForm(forms.ModelForm):
    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = AuthorizationBackgroundCheck
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employee_printed_name': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Printed Name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class AgreementWithCompanyForm(forms.ModelForm):
    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = AgreementWithCompany
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employee_printed_name': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Printed Name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class DrugTestGuidelinesForm(forms.ModelForm):
    employee_signature_img = JSignatureField()

    class Meta:
        model = DrugTestGuidelines
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employee_printed_name': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Type First Name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class DisclosureDrugTestingForm(forms.ModelForm):
    employee_signature_img = JSignatureField()

    class Meta:
        model = DisclosureDrugTesting
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employee_printed_name': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Type First Name'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class EmployerInformationForm(forms.ModelForm):
    class Meta:
        model = EmployerInformation
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                           'placeholder': 'First Name'}),
            'business': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Name'}),
            'fein': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'FEIN'}),
            'physical_address': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                       'placeholder': 'Physical Address'}),
            'mail_address': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                   'placeholder': 'example@gmail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                            'placeholder': 'City'}),
        }


class NoticeAcknowledgementForm(forms.ModelForm):
    is_at_hiring = forms.BooleanField(required=False, initial=True)
    is_before_change = forms.BooleanField(required=False, initial=False)
    is_allowance_none = forms.BooleanField(required=False, initial=True)
    is_tips_allowance_ = forms.BooleanField(required=False, initial=False)
    is_allowance_meals = forms.BooleanField(required=False, initial=False)
    is_allowance_loading = forms.BooleanField(required=False, initial=False)
    is_allowance_other = forms.BooleanField(required=False, initial=False)
    is_weekly = forms.BooleanField(required=False, initial=True)
    is_pay_bi_weekly = forms.BooleanField(required=False, initial=False)
    is_pay_other = forms.BooleanField(required=False, initial=False)
    is_notice_english = forms.BooleanField(required=False, initial=True)
    is_my_primary_language = forms.BooleanField(required=False, initial=False)

    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = NoticeAcknowledgement
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'employee_rates_a_2': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_rates_b_2': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_rates_c_2': forms.TextInput(attrs={'class': 'form-control'}),
            'allowance_loading': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'allowance_other': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'regular_payday': forms.TextInput(attrs={'class': 'form-control'}),
            'pay_other': forms.TextInput(attrs={'class': 'form-control', 'disabled': True}),
            'primary_language': forms.TextInput(attrs={'class': 'form-control'}),
            'employee_printed_name': forms.TextInput(attrs={'class': 'form-control bottom-border',
                                                            'placeholder': 'Employee Printed Name'}),
            'papers_name_title': forms.TextInput(attrs={'class': 'form-control bottom-border',
                                                        'placeholder': "Preparer\'s Name Title"}),
            'employee_rates_a_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'employee_rates_b_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'employee_rates_c_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'wage_parity_rates_a': forms.NumberInput(attrs={'class': 'form-control'}),
            'wage_parity_rates_b': forms.NumberInput(attrs={'class': 'form-control'}),
            'wage_parity_rates_c': forms.NumberInput(attrs={'class': 'form-control'}),
            'allowance_tips': forms.NumberInput(attrs={'class': 'form-control', 'disabled': True}),
            'allowance_meals': forms.NumberInput(attrs={'class': 'form-control', 'disabled': True}),
            'single_pay_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'wage_parity_pay_rates': forms.NumberInput(attrs={'class': 'form-control'}),
            'multiple_pay_rates': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control bottom-border'}),
        }


class BenefitPortionCompensationForm(forms.ModelForm):
    class Meta:
        model = BenefitPortionCompensation
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'type_of_supplement1': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'type_of_supplement2': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'type_of_supplement3': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'provider_name_address1': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'provider_name_address2': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'provider_name_address3': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'agreement_info1': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'agreement_info2': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'agreement_info3': forms.TextInput(attrs={'class': 'form-control remove-border'}),
            'obtained_by': forms.TextInput(attrs={'class': 'form-control  mb-3'}),
            'hourly_rate1': forms.NumberInput(attrs={'class': 'form-control remove-border'}),
            'hourly_rate2': forms.NumberInput(attrs={'class': 'form-control remove-border'}),
            'hourly_rate3': forms.NumberInput(attrs={'class': 'form-control remove-border'}),
        }


class EmployeeAcknowledgementForm(forms.ModelForm):
    CHOICES = [('True', 'Yes'),
               ('False', 'No')]

    is_notice_given = forms.ChoiceField(choices=CHOICES, initial=True, widget=forms.RadioSelect)

    employee_signature_img = JSignatureField(required=True)

    class Meta:
        model = EmployeeAcknowledgement
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'primary_language': forms.TextInput(attrs={'class': 'form-control', 'readonly': True,
                                                       'placeholder': 'Primary Language'}),
            'employee_printed_name': forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Employee Printed Name'}),
            'papers_name_title': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Papers Name Title'}),
            'sign_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class DepositAuthorizationForm(forms.ModelForm):
    CHOICES = [('True', 'Checking'),
               ('False', 'Savings')]

    type_of_account = forms.ChoiceField(choices=CHOICES, initial=True, widget=forms.RadioSelect)

    employee_signature_img = JSignatureField()

    class Meta:
        model = DepositAuthorization
        exclude = ('created_by', 'created_at', 'updated_at', 'updated_by')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Address'}),
            'city_state_zip': forms.TextInput(attrs={'class': 'form-control',
                                                     'placeholder': 'City, State, Zip Code'}),
            'name_of_bank': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Name of Bank'}),
            'account': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Account'}),
            'digit_routing': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Digit Routing'}),
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
