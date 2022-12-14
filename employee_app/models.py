from django.db import models
from django.utils import timezone
from jsignature.fields import JSignatureField


# Create your models here.
class Employee(models.Model):
    objects = None

    employee_name = models.CharField(max_length=250, null=True)
    date_of_service = models.DateTimeField(null=False)
    # signature = JSignatureField(max_length=1000, default=None)
    medicaid_id = models.IntegerField(null=True, blank=True)
    mobile_no = models.CharField(max_length=250, null=True)
    pa_name = models.CharField(max_length=250, null=True, default=None)
    employee_id = models.IntegerField(primary_key=True, null=False, blank=True, default=None)
    is_active = models.BooleanField(null=True, default=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


# Create your models here.
class DemoUser(models.Model):
    objects = None

    employee_name = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(null=False)
    signature = JSignatureField(max_length=1000, default=None)
    medicaid_id = models.IntegerField(null=True, blank=True)
    mobile_no = models.CharField(max_length=250, null=True)
    pa_name = models.CharField(max_length=250, null=True, default=None)
    employee_id = models.IntegerField(primary_key=True, null=False, blank=True, default=None)
    is_active = models.BooleanField(null=True, default=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class SignatureModel(models.Model):
    signature = JSignatureField(max_length=1000)


class Demographics(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="demographics", null=True,
                                 blank=True, default=None)

    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    social_security_number = models.IntegerField(null=True, blank=True)
    street_address = models.CharField(max_length=250, null=True, blank=True)
    city_town = models.CharField(max_length=250, null=True, blank=True)
    state_zip_code = models.IntegerField(null=True, blank=True)
    home_phone = models.CharField(max_length=250, null=True, blank=True)
    cell_phone = models.CharField(max_length=250, null=True, default=None)

    created_by = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class HoursAvailable(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="hoursavailable", null=True,
                                 blank=True, default=None)

    is_day = models.BooleanField(null=True, blank=True, default=False)
    is_night = models.BooleanField(null=True, blank=True, default=False)
    is_live_in = models.BooleanField(null=True, blank=True, default=False)
    is_saturday = models.BooleanField(null=True, blank=True, default=False)
    is_sunday = models.BooleanField(null=True, blank=True, default=False)
    is_monday = models.BooleanField(null=True, blank=True, default=False)
    is_tuesday = models.BooleanField(null=True, blank=True, default=False)
    is_wednesday = models.BooleanField(null=True, blank=True, default=False)
    is_thursday = models.BooleanField(null=True, blank=True, default=False)
    is_friday = models.BooleanField(null=True, blank=True, default=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class Education(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="education",
                                 null=True, blank=True, default=None)

    high_school_name = models.CharField(max_length=600, null=True, blank=True)
    high_school_city_state = models.CharField(max_length=600, null=True, blank=True)
    college = models.CharField(max_length=600, null=True, blank=True)
    college_city_state = models.CharField(max_length=600, null=True, blank=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class ProfessionalTraining(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="professionaltraining", null=True,
                                 blank=True)

    name_of_school_city_state = models.CharField(max_length=350, null=True, blank=True)
    entrance_date = models.DateTimeField(null=True, blank=True, default=None)
    is_graduate = models.BooleanField(null=False, blank=True)
    certificate_degree = models.CharField(max_length=500, null=True, blank=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class SkillsChecklist(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="skillschecklist", null=True,
                                 blank=True)

    is_home_care = models.BooleanField(null=True, blank=True, default=False)
    is_denture_care = models.BooleanField(null=True, blank=True, default=False)
    is_non_sterile_dressing = models.BooleanField(null=True, blank=True, default=False)
    is_orthopedics = models.BooleanField(null=True, blank=True, default=False)
    is_special_diets = models.BooleanField(null=True, blank=True, default=False)
    is_range_of_motion = models.BooleanField(null=True, blank=True, default=False)
    is_vital_signs = models.BooleanField(null=True, blank=True, default=False)
    is_diabetes_care = models.BooleanField(null=True, blank=True, default=False)
    is_kosher_cooking = models.BooleanField(null=True, blank=True, default=False)
    is_transfer_techniques = models.BooleanField(null=True, blank=True, default=False)
    is_urine_testing = models.BooleanField(null=True, blank=True, default=False)
    is_patient_teaching = models.BooleanField(null=True, blank=True, default=False)
    is_household_maintenance = models.BooleanField(null=True, blank=True, default=False)
    is_hoyer_lift = models.BooleanField(null=True, blank=True, default=False)
    is_geriatrics = models.BooleanField(null=True, blank=True, default=False)
    other1 = models.CharField(max_length=500, null=True, blank=True, default=None)
    is_laundry = models.BooleanField(null=True, blank=True, default=False)
    is_foyer_lift = models.BooleanField(null=True, blank=True, default=False)
    is_child_care = models.BooleanField(null=True, blank=True, default=False)
    other2 = models.CharField(max_length=500, null=True, blank=True, default=None)
    is_bed_bath = models.BooleanField(null=True, blank=True, default=False)
    is_ostomy_care = models.BooleanField(null=True, blank=True, default=False)
    is_newborn_care = models.BooleanField(null=True, blank=True, default=False)
    other3 = models.CharField(max_length=500, null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class Transportation(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="transportation", null=True,
                                 blank=True)

    is_bus_train_car = models.BooleanField(null=True, default=False, blank=True)
    routes = models.CharField(max_length=500, null=True, blank=True, default='')
    is_valid_licenses = models.BooleanField(null=True, default=False, blank=True)
    is_permission_for_criminal_background = models.BooleanField(null=True, default=False, blank=True)
    is_personal_assistant_guide = models.BooleanField(null=True, default=False, blank=True)
    printed_name = models.CharField(max_length=250, null=True, blank=True, default=None)
    signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class EmployeeWithholdingCertificate(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employeewithholdingcertificate",
                                 null=True, blank=True)

    first_middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    social_security_number = models.IntegerField(null=False)
    address = models.CharField(max_length=500, null=True)
    city_town_state_zip = models.CharField(max_length=500, null=True)
    is_single_or_married = models.BooleanField(null=False, default=True)
    is_married_jointly = models.BooleanField(null=False, default=True)
    is_head_of_household = models.BooleanField(null=False, default=True)
    is_two_jobs_total = models.BooleanField(null=False, default=True)
    children_under_age = models.IntegerField(null=False)
    others_dependents = models.IntegerField(null=False)
    total = models.IntegerField(null=False)
    other_income = models.IntegerField(null=False)
    deductions = models.IntegerField(null=False)
    extra_withholding = models.IntegerField(null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)
    employer_name_address = models.CharField(max_length=500, null=True)
    first_date_of_employment = models.DateTimeField(null=True, blank=True, default=None)
    employer_identification_no = models.IntegerField(null=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class EmployeeWithholdingAllowanceCertificate(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="withholdingallowance", null=True,
                                 blank=True)

    first_middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    social_security_number = models.IntegerField(null=False)
    permanent_home_address = models.CharField(max_length=500, null=True)
    apartment_no = models.IntegerField(null=False)
    city_village_post_office = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=300, null=True)
    zip_code = models.IntegerField(null=False)
    is_single_or_head_of_household = models.BooleanField(null=False, default=True)
    is_married = models.BooleanField(null=False, default=True)
    is_married_higher_single_rate = models.BooleanField(null=False, default=True)
    is_new_york_resident = models.BooleanField(null=False, default=True)
    is_yonkers_resident = models.BooleanField(null=False, default=True)
    total_newyork_yonkers_allowance = models.IntegerField(null=False)
    total_newyork_allowance = models.IntegerField(null=False)
    new_york_state_amount = models.IntegerField(null=False)
    new_york_city_amount = models.IntegerField(null=False)
    yonkers_amount = models.IntegerField(null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)
    is_exemption_allowances = models.BooleanField(null=False, default=True)
    is_new_hire = models.BooleanField(null=False, default=True)
    employee_performed_date = models.DateTimeField(null=True, blank=True, default=None)
    is_health_insurance = models.BooleanField(null=False, default=True)
    employee_qualifies_date = models.DateTimeField(null=True, blank=True, default=None)
    employer_name_address = models.CharField(max_length=600, null=True)
    employer_identification_no = models.IntegerField(null=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class EmployeeInformationAttestation(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="informationattestation", null=True,
                                 blank=True)

    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=150, null=True)
    other_name = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=800, null=True)
    apt_no = models.IntegerField(null=False)
    city_town = models.CharField(max_length=800, null=True)
    state = models.CharField(max_length=500, null=True)
    zip_code = models.IntegerField(null=False)
    date_of_birth = models.DateTimeField(null=True, blank=True, default=None)
    social_security_no = models.IntegerField(null=False)
    employee_email_address = models.EmailField(max_length=150, blank=True, null=True, unique=True)
    employee_tp_no = models.CharField(max_length=15, null=True)
    is_citizen_us = models.BooleanField(null=False, default=True)
    is_non_citizen_us = models.BooleanField(null=False, default=True)
    is_lawful_resident = models.BooleanField(null=False, default=True)
    authorize_to_work = models.CharField(max_length=500, null=False)
    alien_reg_no = models.IntegerField(null=False)
    admission_no = models.IntegerField(null=False)
    foreign_passport_no = models.IntegerField(null=False)
    country_of_issuance = models.CharField(max_length=500, null=False)
    or_code = models.IntegerField(null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    today_date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class TranslatorCertificate(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="translator", null=True, blank=True)

    is_use_translator = models.BooleanField(null=False, default=True)
    is_preparer_assisted = models.BooleanField(null=False, default=True)
    preparer_signature_img = JSignatureField(max_length=1000, default=None)
    today_date = models.DateTimeField(null=True, blank=True, default=None)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=800, null=True)
    city = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=500, null=True)
    zip_code = models.IntegerField(null=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class EmployerReviewVerification(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employerreviewr", null=True,
                                 blank=True)

    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=150, null=True)
    mi = models.CharField(max_length=150, null=True)
    citizenship_status = models.CharField(max_length=150, null=True)

    document_title_list_a_1 = models.CharField(max_length=150, null=True)
    issuing_authority_list_a_1 = models.CharField(max_length=150, null=True)
    document_no_e_list_a_1 = models.CharField(max_length=150, null=True)
    expire_date_e_list_a_1 = models.DateTimeField(null=True, blank=True, default=None)

    document_title_list_a_2 = models.CharField(max_length=150, null=True)
    issuing_authority_list_a_2 = models.CharField(max_length=150, null=True)
    document_no_e_list_a_2 = models.CharField(max_length=150, null=True)
    expire_date_e_list_a_2 = models.DateTimeField(null=True, blank=True, default=None)

    document_title_list_a_3 = models.CharField(max_length=150, null=True)
    issuing_authority_list_a_3 = models.CharField(max_length=150, null=True)
    document_no_e_list_a_3 = models.CharField(max_length=150, null=True)
    expire_date_e_list_a_3 = models.DateTimeField(null=True, blank=True, default=None)

    document_title_list_b = models.CharField(max_length=150, null=True)
    issuing_authority_list_b = models.CharField(max_length=150, null=True)
    document_no_e_list_b = models.CharField(max_length=150, null=True)
    expire_date_e_list_b = models.DateTimeField(null=True, blank=True, default=None)

    document_title_list_c = models.CharField(max_length=150, null=True)
    issuing_authority_list_c = models.CharField(max_length=150, null=True)
    document_no_e_list_c = models.CharField(max_length=150, null=True)
    expire_date_e_list_c = models.DateTimeField(null=True, blank=True, default=None)
    additional_info_b_n_c = models.CharField(max_length=1000, null=True)
    qr_code = models.CharField(max_length=100, null=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class EmploymentFirstDay(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employmentfirstday", null=True,
                                 blank=True)

    employee_signature_img = JSignatureField(max_length=1000, default=None)
    today_date = models.DateTimeField(null=True, blank=True, default=None)
    employer_title = models.CharField(max_length=200, null=False)
    employer_first_name = models.CharField(max_length=200, null=True)
    employer_last_name = models.CharField(max_length=200, null=True)
    business_organization_name = models.CharField(max_length=800, null=True)
    business_organization_address = models.CharField(max_length=1000, null=True)
    city_town = models.CharField(max_length=500, null=True)
    state = models.CharField(max_length=500, null=True)
    zip_code = models.IntegerField(null=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class ReverificationRehires(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="reverificationrehires", null=True,
                                 blank=True)

    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=200, null=True)
    date_of_rehire = models.DateTimeField(null=True, blank=True, default=None)
    document_title = models.CharField(max_length=150, null=True)
    document_no = models.CharField(max_length=150, null=True)
    expire_date = models.DateTimeField(null=True, blank=True, default=None)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    today_date = models.DateTimeField(null=True, blank=True, default=None)
    employer_name = models.CharField(max_length=150, null=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class AcknowledgementOfReceipt(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="acknowledgementreceipt", null=True,
                                 blank=True)

    employee_printed_name = models.CharField(max_length=150, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class VoluntaryIdentification(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="voluntaryidentification", null=True,
                                 blank=True)

    first_name = models.CharField(max_length=200, null=False)
    middle_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    business_unit_location = models.CharField(max_length=600, null=False)
    department = models.CharField(max_length=500, null=False)
    job_title_position = models.CharField(max_length=400, null=False)
    date = models.DateTimeField(null=True, blank=True, default=None)
    is_male = models.BooleanField(null=False, default=True)
    is_female = models.BooleanField(null=False, default=True)
    is_disclose_sex = models.BooleanField(null=False, default=True)
    is_hispanic_or_latino = models.BooleanField(null=False, default=True)
    is_middle_or_north_east = models.BooleanField(null=False, default=True)
    is_black_or_african_American = models.BooleanField(null=False, default=True)
    is_other_pacific_island = models.BooleanField(null=False, default=True)
    is_asian = models.BooleanField(null=False, default=True)
    is_american_indian_or_alaskan = models.BooleanField(null=False, default=True)
    is_two_or_more_races = models.BooleanField(null=False, default=True)
    is_disclose_info = models.BooleanField(null=False, default=True)
    is_disabled_veteran = models.BooleanField(null=False, default=True)
    date_of_active_duty = models.DateTimeField(null=True, blank=True, default=None)
    is_armed_forces = models.BooleanField(null=False, default=True)
    is_other_protected_veteran = models.BooleanField(null=False, default=True)
    military_discharge_date = models.DateTimeField(null=True, blank=True, default=None)
    is_disclose_military_status = models.BooleanField(null=False, default=True)
    is_no_military_status = models.BooleanField(null=False, default=True)
    is_have_disability = models.BooleanField(null=False, default=True)
    is_no_disability = models.BooleanField(null=False, default=True)
    is_disclose_disability = models.BooleanField(null=False, default=True)
    nature_of_disability = models.CharField(max_length=800, null=False)
    voluntarily_info = models.CharField(max_length=1000, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    sign_date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class AuthorizationBackgroundCheck(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="backgroundcheck", null=True,
                                 blank=True)

    employee_printed_name = models.CharField(max_length=200, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class AgreementWithCompany(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="agreement", null=True, blank=True)

    employee_printed_name = models.CharField(max_length=100, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class DrugTestGuidelines(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="drugtestguidelines", null=True,
                                 blank=True)

    employee_printed_name = models.CharField(max_length=200, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class DisclosureDrugTesting(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="disclosuredrugtesting", null=True,
                                 blank=True)

    employee_printed_name = models.CharField(max_length=100, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class EmployerInformation(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employerinformation", null=True,
                                 blank=True)

    name = models.CharField(max_length=250, null=False)
    business = models.CharField(max_length=800, null=False)
    fein = models.CharField(max_length=400, null=True)
    physical_address = models.CharField(max_length=800, null=False)
    mail_address = models.EmailField(max_length=250, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=15, null=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class NoticeAcknowledgement(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="noticeacknowledgement", null=True,
                                 blank=True)

    is_at_hiring = models.BooleanField(null=False, default=True)
    is_before_change = models.BooleanField(null=False, default=True)
    employee_rates = models.IntegerField(null=False)
    wage_parity_rates = models.IntegerField(null=False)
    is_none = models.BooleanField(null=False, default=True)
    tips = models.IntegerField(null=False)
    meals = models.IntegerField(null=False)
    loading = models.CharField(max_length=200, null=False)
    allowance_other = models.CharField(max_length=200, null=False)
    regular_payday = models.CharField(max_length=200, null=False)
    is_weekly = models.BooleanField(null=False, default=True)
    is_bi_weekly = models.BooleanField(null=False, default=True)
    pay_other = models.CharField(max_length=200, null=False)
    single_pay_rate = models.IntegerField(null=False)
    wage_parity_pay_rates = models.IntegerField(null=False)
    multiple_pay_rates = models.IntegerField(null=False)
    is_notice_in_english = models.BooleanField(null=False, default=True)
    primary_language = models.CharField(max_length=100, null=False)
    employee_printed_name = models.CharField(max_length=100, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)
    papers_name_title = models.CharField(max_length=200, null=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class BenefitPortionCompensation(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="benefitportioncompensation",
                                 null=True, blank=True)

    hourly_rate = models.IntegerField(null=False)
    type_of_supplement = models.CharField(max_length=500, null=False)
    provider_name_address = models.CharField(max_length=800, null=False)
    agreement_info = models.CharField(max_length=1000, null=False)
    obtained_by = models.CharField(max_length=400, null=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class EmployeeAcknowledgement(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="employeeacknowledgement", null=True,
                                 blank=True)

    primary_language = models.CharField(max_length=250, null=False)
    is_notice_given = models.BooleanField(null=False, default=True)
    employee_printed_name = models.CharField(max_length=200, null=False)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    sign_date = models.DateTimeField(null=True, blank=True, default=None)
    papers_name_title = models.CharField(max_length=500, null=False)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)


class DepositAuthorization(models.Model):
    objects = None

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="depositauthorization", null=True,
                                 blank=True)

    name = models.CharField(max_length=500, null=False)
    address = models.CharField(max_length=800, null=False)
    city_state_zip = models.CharField(max_length=600, null=False)
    name_of_bank = models.CharField(max_length=500, null=False)
    account = models.IntegerField(null=False)
    digit_routing = models.IntegerField(null=False)
    is_checking = models.BooleanField(null=False, default=True)
    is_savings = models.BooleanField(null=False, default=True)
    employee_signature_img = JSignatureField(max_length=1000, default=None)
    date = models.DateTimeField(null=True, blank=True, default=None)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
