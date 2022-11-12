from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from .models import *
from django.contrib import messages
from employee_app.forms import *
from admin_app.models import Users
from employee_app.models import *
from admin_app.forms import UserForm
from jsignature.utils import draw_signature
import datetime
from datetime import datetime
from admin_app.aes_cipher import AESCipher
from validate_email_address import validate_email

""" emp_info = Employees.objects.get(pk=1)
    emp_form = EmployeeForm(initial={'name': emp_info.name}) """

""" Login View """


class LoginView(View):

    @staticmethod
    def get(request):
        try:
            request.session.flush()
            return render(request, 'employee/log-in.html')
        except Exception as e:
            print(e)
            return render(request, 'employee/log-in.html', )

    @staticmethod
    def post(request):
        try:
            request.session.flush()

            user_id = request.POST.get('email').strip()
            password = request.POST.get('password').strip()

            if validate_email(user_id):
                if Users.objects.filter(email=user_id).exists():
                    # admin login
                    user = Users.objects.get(email=user_id)

                    db_pass = eval(user.password)
                    decoded_pass = AESCipher().decrypt(db_pass)
                    if password == decoded_pass and user_id == user.email:
                        if user.is_admin is True and user.is_employee:
                            if user.is_active:
                                request.session['admin'] = user.employee_id
                                messages.success(request, 'Login Successful!')
                                return redirect("create_employee_user_admin")
                            else:
                                messages.error(request, 'User is not Active!!')
                                return redirect("login")
                        elif user.is_super_admin is True:
                            if user.is_active:
                                request.session['super_admin'] = user.employee_id
                                messages.success(request, 'Super Admin Login Successful!')
                                return redirect("create_employee_user_super_admin")
                            else:
                                messages.error(request, 'User is not Active!!')
                                return redirect("login")
                        else:
                            messages.error(request, 'User Role is not Defined!!')
                            return redirect("login")
                    else:
                        messages.error(request, 'User Password or Email Does Not Matched!!')
                        return redirect("login")
                else:
                    messages.error(request, 'User Does not Exits!!')
                    return redirect("login")

            elif Users.objects.filter(employee_id=user_id).exists():
                user = Users.objects.get(employee_id=user_id)
                # Employee login
                db_pass = eval(user.password)
                decoded_pass = AESCipher().decrypt(db_pass)

                if password == decoded_pass and int(user_id) == user.employee_id:
                    if user.is_employee is True:
                        if user.is_active:
                            request.session['employee'] = user.employee_id
                            messages.success(request, 'Login Successful!')
                            return redirect("index", user_id)
                        else:
                            messages.error(request, 'User is not Active!!')
                            return redirect('login')
                    else:
                        messages.error(request, 'User is not Employee!!')
                        return redirect('login')
                else:
                    messages.error(request, 'User Password or Email Does Not Matched!!')
                    return redirect('login')
            else:
                messages.error(request, 'User Does Not Exits!')
                return redirect('login')
        except Exception as e:
            print(e)
            messages.error(request, 'Something went wrong, Check your login Credentials!!')
            return redirect('login')


class CreateEmployeeProfile(View):

    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee') or request.GET.get('user_id'):

                user_id = request.GET.get('user_id')
                employee = request.session.get('employee')
                admin = request.session.get('admin')
                super_admin = request.session.get('super_admin')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_id:
                    user_role = Users.objects.get(employee_id=user_id)
                    if user_role.is_admin:
                        admin = user_role.employee_id
                        employee = user_role.employee_id
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        super_admin = user_role.employee_id
                        employee = user_role.employee_id
                        is_super_admin = user_role.is_super_admin
                    else:
                        employee = user_role.employee_id
                        is_employee = user_role.is_employee

                else:
                    user_role = Users.objects.get(employee_id=employee)
                    if user_role.is_admin:
                        admin = user_role.employee_id
                        employee = user_role.employee_id
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        super_admin = user_role.employee_id
                        employee = user_role.employee_id
                        is_super_admin = user_role.is_super_admin
                    else:
                        employee = user_role.employee_id
                        is_employee = user_role.is_employee

                user = Users.objects.get(employee_id=employee_id)

                user_form = EmployeeForm(readonly_form=True, initial={
                    'employee_name': user.employee_name,
                    'date_of_service': user.date_of_service,
                    'medicaid_id': user.medicaid_id,
                    'pa_name': user.pa_name,
                    'employee_id': user.employee_id,
                    'mobile_no': user.mobile_no,
                    'is_admin': is_admin,
                    'is_pagination': is_pagination,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'nid_img': user.nid_img,
                    'employee_img': user.employee_img,

                })

                if not Transportation.objects.filter(employee_id=employee_id).exists():
                    demographics_form = DemographicsForm()
                    hours_available_form = HoursAvailableForm()
                    education_form = EducationForm()
                    training_form = ProfessionalTrainingForm()
                    skills_form = SkillsChecklistForm()
                    transportation_form = TransportationForm()
                    if demographics_form and hours_available_form and education_form and training_form \
                            and skills_form and transportation_form:

                        context = {
                            'employee_id': employee_id,
                            'user_form': user_form,
                            'demographics_form': demographics_form,
                            'hours_available_form': hours_available_form,
                            'education_form': education_form,
                            'training_form': training_form,
                            'skills_form': skills_form,
                            'transportation_form': transportation_form,
                            'is_admin': is_admin,
                            'is_pagination': is_pagination,
                            'is_super_admin': is_super_admin,
                            'is_employee': is_employee,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
                            'page1': 'active',
                            'is_pagination': is_pagination,
                        }
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        return render(request, "employee/index.html", context)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'user_form': user_form,
                            'demographics_form': demographics_form,
                            'hours_available_form': hours_available_form,
                            'education_form': education_form,
                            'training_form': training_form,
                            'skills_form': skills_form,
                            'transportation_form': transportation_form,
                            'is_admin': is_admin,
                            'is_pagination': is_pagination,
                            'is_super_admin': is_super_admin,
                            'is_employee': is_employee,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
                            'page1': 'active',
                            'is_pagination': is_pagination,
                        }
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        return render(request, "employee/index.html", context)
                elif Transportation.objects.filter(employee_id=employee_id).exists():
                    user = Users.objects.get(employee_id=employee_id)
                    demographics = Demographics.objects.get(employee_id=employee_id)
                    hours_available = HoursAvailable.objects.get(employee_id=employee_id)
                    education = Education.objects.get(employee_id=employee_id)
                    training = ProfessionalTraining.objects.get(employee_id=employee_id)
                    skills = SkillsChecklist.objects.get(employee_id=employee_id)
                    transportation = Transportation.objects.get(employee_id=employee_id)

                    if user and demographics and hours_available and education \
                            and training and skills and transportation:
                        user_form = EmployeeForm(instance=user, readonly_form=True)
                        demographics_form = DemographicsForm(instance=demographics)
                        hours_available_form = HoursAvailableForm(instance=hours_available)
                        education_form = EducationForm(instance=education)
                        training_form = ProfessionalTrainingForm(instance=training)
                        skills_form = SkillsChecklistForm(instance=skills)
                        transportation_form = TransportationForm(instance=transportation)

                        context = {
                            'employee_id': employee_id,
                            'user_form': user_form,
                            'demographics_form': demographics_form,
                            'hours_available_form': hours_available_form,
                            'education_form': education_form,
                            'training_form': training_form,
                            'skills_form': skills_form,
                            'transportation_form': transportation_form,
                            'is_admin': is_admin,
                            'is_pagination': is_pagination,
                            'is_super_admin': is_super_admin,
                            'is_employee': is_employee,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
                            'page1': 'active',

                        }
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        return render(request, "employee/index.html", context)
                else:
                    demographics_form = DemographicsForm()
                    hours_available_form = HoursAvailableForm()
                    education_form = EducationForm()
                    training_form = ProfessionalTrainingForm()
                    skills_form = SkillsChecklistForm()
                    transportation_form = TransportationForm()
                    if demographics_form and hours_available_form and education_form and training_form \
                            and skills_form and transportation_form:
                        context = {
                            'employee_id': employee_id,
                            'user_form': user_form,
                            'demographics_form': demographics_form,
                            'hours_available_form': hours_available_form,
                            'education_form': education_form,
                            'training_form': training_form,
                            'skills_form': skills_form,
                            'transportation_form': transportation_form,
                            'is_admin': is_admin,
                            'is_pagination': is_pagination,
                            'is_super_admin': is_super_admin,
                            'is_employee': is_employee,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
                            'page1': 'active',
                        }
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        return render(request, "employee/index.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                employee_id = employee_id
                demographics_form = DemographicsForm(request.POST or None)
                hours_available_form = HoursAvailableForm(request.POST or None)
                education_form = EducationForm(request.POST or None)
                training_form = ProfessionalTrainingForm(request.POST or None)
                skills_form = SkillsChecklistForm(request.POST or None)
                transportation_form = TransportationForm(request.POST or None)

                if request.method == "POST" and not Transportation.objects.filter(
                        employee_id=employee_id).exists() and demographics_form.is_valid() \
                        and hours_available_form.is_valid() and education_form.is_valid() and training_form.is_valid() \
                        and skills_form.is_valid() and transportation_form.is_valid():

                    # demographics_form
                    demographics = demographics_form.save(commit=False)
                    demographics.employee_id = employee_id
                    demographics.created_by = user_name
                    demographics_form.save()

                    # hours_available_form
                    hours_available = hours_available_form.save(commit=False)
                    hours_available.employee_id = employee_id
                    hours_available.created_by = user_name
                    hours_available.save()

                    # education_form
                    education = education_form.save(commit=False)
                    education.employee_id = employee_id
                    education.created_by = user_name
                    education.save()

                    # training_form
                    training = training_form.save(commit=False)
                    training.employee_id = employee_id
                    training.created_by = user_name
                    training.save()

                    # training_form
                    skills = skills_form.save(commit=False)
                    skills.employee_id = employee_id
                    skills.created_by = user_name
                    skills.save()

                    # transportation_form
                    transportation = transportation_form.save(commit=False)
                    transportation.employee_id = employee_id
                    transportation.created_by = user_name
                    transportation.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('section_w4', employee_id)
                elif request.method == 'POST':
                    demographics = Demographics.objects.get(employee_id=employee_id)
                    demographics_form = DemographicsForm(data=request.POST, instance=demographics)
                    if demographics_form.is_valid():
                        demographics = demographics_form.save(commit=False)
                        demographics.employee_id = employee_id
                        demographics.updated_at = datetime.now()
                        demographics_form.save()

                        hours_available = HoursAvailable.objects.get(employee_id=employee_id)

                        hours_available_form = HoursAvailableForm(data=request.POST, instance=hours_available)
                        if hours_available_form.is_valid():
                            hours_available = hours_available_form.save(commit=False)
                            hours_available.employee_id = employee_id
                            hours_available.updated_by = user_name
                            hours_available.updated_at = datetime.now()
                            hours_available.save()

                            education = Education.objects.get(employee_id=employee_id)
                            education_form = EducationForm(data=request.POST, instance=education)
                            if education_form.is_valid():
                                education = education_form.save(commit=False)
                                education.employee_id = employee_id
                                education.updated_by = user_name
                                education.updated_at = datetime.now()
                                education.save()

                                training = ProfessionalTraining.objects.get(employee_id=employee_id)
                                training_form = ProfessionalTrainingForm(data=request.POST, instance=training)
                                if training_form.is_valid():
                                    training = training_form.save(commit=False)
                                    training.employee_id = employee_id
                                    training.updated_by = user_name
                                    training.updated_at = datetime.now()
                                    training.save()

                                    skills = SkillsChecklist.objects.get(employee_id=employee_id)
                                    skills_form = SkillsChecklistForm(data=request.POST, instance=skills)
                                    if skills_form.is_valid():
                                        skills = skills_form.save(commit=False)
                                        skills.employee_id = employee_id
                                        skills.updated_by = user_name
                                        skills.updated_at = datetime.now()
                                        skills.save()

                                        transportation = Transportation.objects.get(employee_id=employee_id)
                                        transportation_form = TransportationForm(data=request.POST,
                                                                                 instance=transportation)
                                        if transportation_form.is_valid():
                                            transportation = transportation_form.save(commit=False)
                                            transportation.employee_id = employee_id
                                            transportation.updated_by = user_name
                                            transportation.updated_at = datetime.now()
                                            transportation.save()
                                            messages.success(request, 'Step 2!!')
                                            request.session['employee'] = user_name
                                            messages.success(request, 'Data Submission Successful!!')
                                            return redirect('section_w4', employee_id)
                                        else:
                                            context = {
                                                'employee_id': employee_id,
                                                'demographics_form': demographics_form,
                                                'hours_available_form': hours_available_form,
                                                'education_form': education_form,
                                                'training_form': training_form,
                                                'skills_form': skills_form,
                                                'transportation_form': transportation_form,
                                            }
                                            request.session['employee'] = user_name
                                            messages.error(request, 'Data Submission Failed!!')
                                            return render(request, "employee/index.html", context)
                                    else:
                                        context = {
                                            'employee_id': employee_id,
                                            'demographics_form': demographics_form,
                                            'hours_available_form': hours_available_form,
                                            'education_form': education_form,
                                            'training_form': training_form,
                                            'skills_form': skills_form,
                                            'transportation_form': transportation_form,
                                        }
                                        request.session['employee'] = user_name
                                        messages.error(request, 'Data Submission Failed!!')
                                        return render(request, "employee/index.html", context)
                                else:
                                    context = {
                                        'employee_id': employee_id,
                                        'demographics_form': demographics_form,
                                        'hours_available_form': hours_available_form,
                                        'education_form': education_form,
                                        'training_form': training_form,
                                        'skills_form': skills_form,
                                        'transportation_form': transportation_form,
                                    }
                                    request.session['employee'] = user_name
                                    messages.error(request, 'Data Submission Failed!!')
                                    return render(request, "employee/index.html", context)
                            else:
                                context = {
                                    'employee_id': employee_id,
                                    'demographics_form': demographics_form,
                                    'hours_available_form': hours_available_form,
                                    'education_form': education_form,
                                    'training_form': training_form,
                                    'skills_form': skills_form,
                                    'transportation_form': transportation_form,
                                }
                                request.session['employee'] = user_name
                                messages.error(request, 'Data Submission Failed!!')
                                return render(request, "employee/index.html", context)
                        else:
                            context = {
                                'employee_id': employee_id,
                                'demographics_form': demographics_form,
                                'hours_available_form': hours_available_form,
                                'education_form': education_form,
                                'training_form': training_form,
                                'skills_form': skills_form,
                                'transportation_form': transportation_form,
                            }
                            request.session['employee'] = user_name
                            messages.error(request, 'Data Submission Failed!!')
                            return render(request, "employee/index.html", context)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'demographics_form': demographics_form,
                            'hours_available_form': hours_available_form,
                            'education_form': education_form,
                            'training_form': training_form,
                            'skills_form': skills_form,
                            'transportation_form': transportation_form,
                        }
                        request.session['employee'] = user_name
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/index.html", context)
                else:
                    context = {
                        'employee_id': employee_id,
                        'demographics_form': demographics_form,
                        'hours_available_form': hours_available_form,
                        'education_form': education_form,
                        'training_form': training_form,
                        'skills_form': skills_form,
                        'transportation_form': transportation_form,
                    }
                    request.session['employee'] = user_name
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/index.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')


class CreateEmployeeProfileW4(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_name:
                    user_role = Users.objects.get(employee_id=user_name)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                    else:
                        is_employee = user_role.is_employee

                if EmployeeWithholdingCertificate.objects.filter(employee_id=employee_id).exists():
                    demographics = Demographics.objects.get(employee_id=employee_id)
                    employee_withholding_certificate = EmployeeWithholdingCertificate.objects.get(
                        employee_id=employee_id)
                    withholding_certificate_form = EmployeeWithholdingCertificateForm(
                        instance=employee_withholding_certificate,
                        initial={
                            'last_name': demographics.last_name,
                            'social_security_number': demographics.social_security_number
                        })

                    context = {
                        'employee_id': employee_id,
                        'withholding_certificate_form': withholding_certificate_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'is_pagination': is_pagination,
                        'page2': 'active',
                    }

                    return render(request, "employee/section_w4.html", context)
                elif Demographics.objects.filter(employee_id=employee_id).exists():
                    demographics = Demographics.objects.get(employee_id=employee_id)
                    withholding_certificate_form = EmployeeWithholdingCertificateForm(initial={
                        'last_name': demographics.last_name,
                        'social_security_number': demographics.social_security_number
                    })

                    # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                    context = {
                        'employee_id': employee_id,
                        'withholding_certificate_form': withholding_certificate_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'is_pagination': is_pagination,
                        'page2': 'active',
                    }
                    messages.success(request, 'Step 2!!')
                    return render(request, "employee/section_w4.html", context)
                else:
                    withholding_certificate_form = EmployeeWithholdingCertificateForm()
                    context = {
                        'employee_id': employee_id,
                        'withholding_certificate_form': withholding_certificate_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'is_pagination': is_pagination,
                        'page2': 'active',
                    }
                    messages.error(request, 'Please fill up page 1 first!')
                    return render(request, "employee/section_w4.html", context)

            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                withholding_certificate_form = EmployeeWithholdingCertificateForm(request.POST or None)
                if not EmployeeWithholdingCertificate.objects.filter(employee_id=employee_id).exists():
                    if request.method == "POST" and withholding_certificate_form.is_valid():
                        employee_id = employee_id

                        # demographics_form
                        withholding_certificate = withholding_certificate_form.save(commit=False)
                        withholding_certificate.employee_id = employee_id
                        withholding_certificate.created_by = user_name
                        withholding_certificate_form.save()
                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('allowance_certificate', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'withholding_certificate_form': withholding_certificate_form,
                        }
                        messages.error(request, 'Form Validation Failed!!')
                        return render(request, "employee/section_w4.html", context)

                elif request.method == 'POST':
                    withholding_certificate = EmployeeWithholdingCertificate.objects.get(employee_id=employee_id)
                    withholding_certificate_form = EmployeeWithholdingCertificateForm(data=request.POST,
                                                                                      instance=withholding_certificate)
                    if withholding_certificate_form.is_valid():
                        withholding_certificate = withholding_certificate_form.save(commit=False)
                        withholding_certificate.employee_id = employee_id
                        withholding_certificate.updated_by = user_name
                        withholding_certificate.updated_at = datetime.now()
                        withholding_certificate.save()
                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('allowance_certificate', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'withholding_certificate_form': withholding_certificate_form,
                        }
                        messages.error(request, 'Form Validation Failed!!')
                        return render(request, "employee/section_w4.html", context)
                else:
                    context = {
                        'employee_id': employee_id,
                        'withholding_certificate_form': withholding_certificate_form,
                    }
                    messages.success(request, 'Step 3!!')
                    return render(request, "employee/section_w4.html", context)
        except Exception as e:
            print(e)
            return redirect('login')


class CreateEmployeeAllowanceCertificate(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_name:
                    user_role = Users.objects.get(employee_id=user_name)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                    else:
                        is_employee = user_role.is_employee

                user_name = request.session.get('employee')
                if EmployeeWithholdingAllowanceCertificate.objects.filter(employee_id=employee_id).exists():
                    demographics = Demographics.objects.get(employee_id=employee_id)
                    employee_withholding_certificate = EmployeeWithholdingCertificate.objects.get(
                        employee_id=employee_id)

                    employee_withholding_allowance_certificate = EmployeeWithholdingAllowanceCertificate.objects.get(
                        employee_id=employee_id)
                    employee_withholding_allowance_certificate_form = EmployeeWithholdingAllowanceCertificateForm(
                        instance=employee_withholding_allowance_certificate,
                        initial={
                            'last_name': demographics.last_name,
                            'social_security_number': demographics.social_security_number,
                            'zip_code': demographics.state_zip_code,
                            'employer_identification_no': employee_withholding_certificate.employer_identification_no,
                        })

                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page3': 'active',
                        'is_pagination': is_pagination,
                    }

                    return render(request, "employee/allowance_certificate.html", context)
                elif Demographics.objects.filter(employee_id=employee_id).exists():
                    demographics = Demographics.objects.get(employee_id=employee_id)
                    employee_withholding_certificate = EmployeeWithholdingCertificate.objects.get(
                        employee_id=employee_id)
                    employee_withholding_allowance_certificate_form = EmployeeWithholdingAllowanceCertificateForm(
                        initial={
                            'last_name': demographics.last_name,
                            'social_security_number': demographics.social_security_number,
                            'zip_code': demographics.state_zip_code,
                            'employer_identification_no': employee_withholding_certificate.employer_identification_no,
                        })

                    # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page3': 'active',
                        'is_pagination': is_pagination,
                    }

                    return render(request, "employee/allowance_certificate.html", context)
                else:
                    employee_withholding_allowance_certificate_form = EmployeeWithholdingAllowanceCertificateForm()

                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page3': 'active',
                        'is_pagination': is_pagination,
                    }
                    messages.error(request, 'Please fill up page 1 first!')
                    return render(request, "employee/allowance_certificate.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        if request.session.get('employee'):
            user_name = request.session.get('employee')
            employee_withholding_allowance_certificate_form = EmployeeWithholdingAllowanceCertificateForm(
                request.POST or None)
            if not EmployeeWithholdingAllowanceCertificate.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and employee_withholding_allowance_certificate_form.is_valid():
                    employee_id = employee_id

                    # demographics_form
                    withholding_allowance_certificate = employee_withholding_allowance_certificate_form.save(
                        commit=False)
                    withholding_allowance_certificate.employee_id = employee_id
                    withholding_allowance_certificate.created_by = user_name
                    employee_withholding_allowance_certificate_form.save()
                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('employee_eligibility_verification', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/allowance_certificate.html", context)

            elif request.method == 'POST':
                withholding_allowance_certificate = EmployeeWithholdingAllowanceCertificate.objects.get(
                    employee_id=employee_id)
                employee_withholding_allowance_certificate_form = EmployeeWithholdingAllowanceCertificateForm(
                    data=request.POST,
                    instance=withholding_allowance_certificate)
                if employee_withholding_allowance_certificate_form.is_valid():
                    allowance_certificate = employee_withholding_allowance_certificate_form.save(commit=False)
                    allowance_certificate.employee_id = employee_id
                    allowance_certificate.updated_by = user_name
                    allowance_certificate.updated_at = datetime.now()
                    allowance_certificate.save()
                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('employee_eligibility_verification', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/allowance_certificate.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                }
                return render(request, "employee/allowance_certificate.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')


class EmployeeEligibilityVerification(View):
    @staticmethod
    def get(request, employee_id):
        if request.session.get('employee'):
            user_name = request.session.get('employee')
            is_admin = False
            is_super_admin = False
            is_employee = False
            is_pagination = False

            if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                is_pagination = True

            if user_name:
                user_role = Users.objects.get(employee_id=user_name)
                if user_role.is_admin:
                    is_admin = user_role.is_admin
                elif user_role.is_super_admin:
                    is_super_admin = user_role.is_super_admin
                else:
                    is_employee = user_role.is_employee

            if EmployeeInformationAttestation.objects.filter(employee_id=employee_id).exists():
                demographics = Demographics.objects.get(employee_id=employee_id)
                employee_withholding_allowance_certificate = EmployeeWithholdingAllowanceCertificate.objects.get(
                    employee_id=employee_id)
                employee_information_attestation = EmployeeInformationAttestation.objects.get(
                    employee_id=employee_id)
                translator_certificate = TranslatorCertificate.objects.get(
                    employee_id=employee_id)

                employee_information_attestation_form = EmployeeInformationAttestationForm(
                    instance=employee_information_attestation,
                    initial={
                        'first_name': demographics.first_name,
                        'last_name': demographics.last_name,
                        'state': employee_withholding_allowance_certificate.state,
                        'apt_no': employee_withholding_allowance_certificate.apartment_no,
                        'zip_code': demographics.state_zip_code,
                    })

                translator_certificate_form = TranslatorCertificateForm(
                    instance=translator_certificate,
                    initial={
                        'first_name': demographics.first_name,
                        'last_name': demographics.last_name,
                        'state': employee_withholding_allowance_certificate.state,
                        'zip_code': demographics.state_zip_code,
                    })

                context = {
                    'employee_id': employee_id,
                    'employee_information_attestation_form': employee_information_attestation_form,
                    'translator_certificate_form': translator_certificate_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page4': 'active',
                    'is_pagination': is_pagination,
                }

                return render(request, "employee/employee-eligibility-verification.html", context)
            elif Demographics.objects.filter(employee_id=employee_id).exists():
                demographics = Demographics.objects.get(employee_id=employee_id)
                employee_withholding_allowance_certificate = EmployeeWithholdingAllowanceCertificate.objects.get(
                    employee_id=employee_id)
                employee_information_attestation_form = EmployeeInformationAttestationForm(
                    initial={
                        'first_name': demographics.first_name,
                        'last_name': demographics.last_name,
                        'state': employee_withholding_allowance_certificate.state,
                        'apt_no': employee_withholding_allowance_certificate.apartment_no,
                        'zip_code': demographics.state_zip_code,
                    })

                translator_certificate_form = TranslatorCertificateForm(
                    initial={
                        'first_name': demographics.first_name,
                        'last_name': demographics.last_name,
                        'state': employee_withholding_allowance_certificate.state,
                        'zip_code': demographics.state_zip_code,
                    })

                # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                context = {
                    'employee_id': employee_id,
                    'employee_information_attestation_form': employee_information_attestation_form,
                    'translator_certificate_form': translator_certificate_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page4': 'active',
                    'is_pagination': is_pagination,
                }
                return render(request, "employee/employee-eligibility-verification.html", context)
            else:
                employee_information_attestation_form = EmployeeInformationAttestationForm()
                translator_certificate_form = TranslatorCertificateForm()

                # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                context = {
                    'employee_id': employee_id,
                    'employee_information_attestation_form': employee_information_attestation_form,
                    'translator_certificate_form': translator_certificate_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page4': 'active',
                    'is_pagination': is_pagination,
                }
                messages.error(request, 'Please fill up page 1 first!')
                return render(request, "employee/employee-eligibility-verification.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')

    @staticmethod
    def post(request, employee_id):

        if request.session.get('employee'):
            user_name = request.session.get('employee')
            employee_information_attestation_form = EmployeeInformationAttestationForm(request.POST or None)
            translator_certificate_form = TranslatorCertificateForm(request.POST or None)
            if not EmployeeInformationAttestation.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and employee_information_attestation_form.is_valid() \
                        and translator_certificate_form.is_valid():
                    employee_id = employee_id
                    employee_information_attestation = employee_information_attestation_form.save(commit=False)
                    employee_information_attestation.employee_id = employee_id
                    employee_information_attestation.created_by = user_name
                    employee_information_attestation.save()

                    translator_certificate = translator_certificate_form.save(commit=False)
                    translator_certificate.employee_id = employee_id
                    translator_certificate.created_by = user_name
                    translator_certificate.save()
                    return redirect('employee_eligibility_verification_part_2', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employee_information_attestation_form': employee_information_attestation_form,
                        'translator_certificate_form': translator_certificate_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/employee-eligibility-verification.html", context)

            elif request.method == 'POST':
                employee_information_attestation = EmployeeInformationAttestation.objects.get(
                    employee_id=employee_id)
                employee_information_attestation_form = EmployeeInformationAttestationForm(
                    data=request.POST,
                    instance=employee_information_attestation)

                translator_certificate = TranslatorCertificate.objects.get(employee_id=employee_id)
                translator_certificate_form = TranslatorCertificateForm(
                    data=request.POST,
                    instance=translator_certificate)

                if employee_information_attestation_form.is_valid() and translator_certificate_form.is_valid():
                    employee_information_attestation = employee_information_attestation_form.save(commit=False)
                    employee_information_attestation.employee_id = employee_id
                    employee_information_attestation.updated_at = datetime.now()
                    employee_information_attestation.updated_by = user_name
                    employee_information_attestation.save()

                    translator_certificate = translator_certificate_form.save(commit=False)
                    translator_certificate.employee_id = employee_id
                    translator_certificate.updated_at = datetime.now()
                    translator_certificate.updated_by = user_name
                    translator_certificate.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('employee_eligibility_verification_part_2', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_information_attestation_form,
                        'translator_certificate_form': translator_certificate_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/employee-eligibility-verification.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'employee_information_attestation_form': employee_information_attestation_form,
                    'translator_certificate_form': translator_certificate_form,
                }
                return render(request, "employee/employee-eligibility-verification.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')


class EmployeeEligibilityVerificationPart2(View):
    @staticmethod
    def get(request, employee_id):
        if request.session.get('employee'):
            user_name = request.session.get('employee')
            is_admin = False
            is_super_admin = False
            is_employee = False
            is_pagination = False

            if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                is_pagination = True

            if user_name:
                user_role = Users.objects.get(employee_id=user_name)
                if user_role.is_admin:
                    is_admin = user_role.is_admin
                elif user_role.is_super_admin:
                    is_super_admin = user_role.is_super_admin
                else:
                    is_employee = user_role.is_employee
            if EmployerReviewVerification.objects.filter(employee_id=employee_id).exists():
                employee_information_attestation = EmployeeInformationAttestation.objects.get(
                    employee_id=employee_id)

                employer_review_verification = EmployerReviewVerification.objects.get(employee_id=employee_id)
                employment_first_day = EmploymentFirstDay.objects.get(employee_id=employee_id)
                reverification_rehires = ReverificationRehires.objects.get(employee_id=employee_id)

                employer_review_verification_form = EmployerReviewVerificationForm(
                    instance=employer_review_verification,
                    initial={
                        'first_name': employee_information_attestation.first_name,
                        'last_name': employee_information_attestation.last_name,
                        'middle_initial': employee_information_attestation.middle_name,
                    })

                employment_first_day_form = EmploymentFirstDayForm(
                    instance=employment_first_day,
                    initial={
                        'city_town': 'Holbrook',
                        'state': 'NY',
                        'zip_code': 11741,
                        'business_organization_name': 'BARI HOME CARE LLC',
                        'business_organization_address': '469 Donald Blvd',
                    }
                )
                reverification_rehires_form = ReverificationRehiresForm(instance=reverification_rehires)

                context = {
                    'employee_id': employee_id,
                    'employer_review_verification_form': employer_review_verification_form,
                    'employment_first_day_form': employment_first_day_form,
                    'reverification_rehires_form': reverification_rehires_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page5': 'active',
                    'is_pagination': is_pagination,
                }

                return render(request, "employee/employee-eligibility-verification_part_2.html", context)
            elif EmployeeInformationAttestation.objects.filter(employee_id=employee_id).exists():
                employee_information_attestation = EmployeeInformationAttestation.objects.get(
                    employee_id=employee_id)

                employer_review_verification_form = EmployerReviewVerificationForm(
                    initial={
                        'first_name': employee_information_attestation.first_name,
                        'last_name': employee_information_attestation.last_name,
                        'middle_initial': employee_information_attestation.middle_name,
                    })

                employment_first_day_form = EmploymentFirstDayForm(initial={
                    'city_town': 'Holbrook',
                    'state': 'NY',
                    'zip_code': 11741,
                    'business_organization_name': 'BARI HOME CARE LLC',
                    'business_organization_address': '469 Donald Blvd',
                })
                reverification_rehires_form = ReverificationRehiresForm()

                # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                context = {
                    'employee_id': employee_id,
                    'employer_review_verification_form': employer_review_verification_form,
                    'employment_first_day_form': employment_first_day_form,
                    'reverification_rehires_form': reverification_rehires_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page5': 'active',
                    'is_pagination': is_pagination,
                }
                return render(request, "employee/employee-eligibility-verification_part_2.html", context)
            else:
                employer_review_verification_form = EmployerReviewVerificationForm()
                employment_first_day_form = EmploymentFirstDayForm(initial={
                    'city_town': 'Holbrook',
                    'state': 'NY',
                    'zip_code': 11741,
                    'business_organization_name': 'BARI HOME CARE LLC',
                    'business_organization_address': '469 Donald Blvd',
                })
                reverification_rehires_form = ReverificationRehiresForm()

                # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                context = {
                    'employee_id': employee_id,
                    'employer_review_verification_form': employer_review_verification_form,
                    'employment_first_day_form': employment_first_day_form,
                    'reverification_rehires_form': reverification_rehires_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page5': 'active',
                    'is_pagination': is_pagination,
                }
                messages.error(request, 'Please fill up page 4 first!')
                return render(request, "employee/employee-eligibility-verification_part_2.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')

    @staticmethod
    def post(request, employee_id):

        if request.session.get('employee'):
            user_name = request.session.get('employee')
            employer_review_verification_form = EmployerReviewVerificationForm(request.POST or None)
            employment_first_day_form = EmploymentFirstDayForm(request.POST or None)
            reverification_rehires_form = ReverificationRehiresForm(request.POST or None)
            if not EmployerReviewVerification.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and employer_review_verification_form.is_valid() \
                        and employment_first_day_form.is_valid() and reverification_rehires_form.is_valid():
                    employee_id = employee_id
                    employer_review_verification = employer_review_verification_form.save(commit=False)
                    employer_review_verification.employee_id = employee_id
                    employer_review_verification.created_by = user_name
                    employer_review_verification.save()

                    employment_first_day = employment_first_day_form.save(commit=False)
                    employment_first_day.employee_id = employee_id
                    employment_first_day.created_by = user_name
                    employment_first_day.save()

                    reverification_rehires = reverification_rehires_form.save(commit=False)
                    reverification_rehires.employee_id = employee_id
                    reverification_rehires.created_by = user_name
                    reverification_rehires.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('personal_assistant_guide_page6', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employer_review_verification_form': employer_review_verification_form,
                        'employment_first_day_form': employment_first_day_form,
                        'reverification_rehires_form': reverification_rehires_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/employee-eligibility-verification_part_2.html", context)

            elif request.method == 'POST':
                employer_review_verification = EmployerReviewVerification.objects.get(employee_id=employee_id)
                employer_review_verification_form = EmployerReviewVerificationForm(
                    data=request.POST,
                    instance=employer_review_verification)

                employment_first_day = EmploymentFirstDay.objects.get(employee_id=employee_id)
                employment_first_day_form = EmploymentFirstDayForm(
                    data=request.POST,
                    instance=employment_first_day)

                reverification_rehires = ReverificationRehires.objects.get(employee_id=employee_id)
                reverification_rehires_form = ReverificationRehiresForm(
                    data=request.POST,
                    instance=reverification_rehires)

                if employer_review_verification_form.is_valid() and employment_first_day_form.is_valid() \
                        and reverification_rehires_form.is_valid():

                    employer_review_verification = employer_review_verification_form.save(commit=False)
                    employer_review_verification.employee_id = employee_id
                    employer_review_verification.updated_at = datetime.now()
                    employer_review_verification.updated_by = user_name
                    employer_review_verification.save()

                    employment_first_day = employment_first_day_form.save(commit=False)
                    employment_first_day.employee_id = employee_id
                    employment_first_day.updated_at = datetime.now()
                    employment_first_day.updated_by = user_name
                    employment_first_day.save()

                    reverification_rehires = reverification_rehires_form.save(commit=False)
                    reverification_rehires.employee_id = employee_id
                    reverification_rehires.updated_at = datetime.now()
                    reverification_rehires.updated_by = user_name
                    reverification_rehires.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('personal_assistant_guide_page6', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employer_review_verification_form': employer_review_verification_form,
                        'employment_first_day_form': employment_first_day_form,
                        'reverification_rehires_form': reverification_rehires_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/employee-eligibility-verification_part_2.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'employer_review_verification_form': employer_review_verification_form,
                    'employment_first_day_form': employment_first_day_form,
                    'reverification_rehires_form': reverification_rehires_form,
                }
                return render(request, "employee/employee-eligibility-verification_part_2.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')


class PersonalAssistantGuidePage6(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_name:
                    user_role = Users.objects.get(employee_id=user_name)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                    else:
                        is_employee = user_role.is_employee

                if AcknowledgementOfReceipt.objects.filter(employee_id=employee_id).exists():
                    acknowledgement_of_receipt = AcknowledgementOfReceipt.objects.get(employee_id=employee_id)
                    acknowledgement_of_receipt_form = AcknowledgementOfReceiptForm(instance=acknowledgement_of_receipt)

                    context = {
                        'employee_id': employee_id,
                        'acknowledgement_of_receipt_form': acknowledgement_of_receipt_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page6': 'active',
                        'is_pagination': is_pagination,
                    }

                    return render(request, "employee/page_six.html", context)
                else:
                    acknowledgement_of_receipt_form = AcknowledgementOfReceiptForm()

                    context = {
                        'employee_id': employee_id,
                        'acknowledgement_of_receipt_form': acknowledgement_of_receipt_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page6': 'active',
                        'is_pagination': is_pagination,
                    }
                    return render(request, "employee/page_six.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                acknowledgement_of_receipt_form = AcknowledgementOfReceiptForm(request.POST or None)
                if not AcknowledgementOfReceipt.objects.filter(employee_id=employee_id).exists():
                    if request.method == "POST" and acknowledgement_of_receipt_form.is_valid():
                        employee_id = employee_id
                        acknowledgement_of_receipt = acknowledgement_of_receipt_form.save(commit=False)
                        acknowledgement_of_receipt.employee_id = employee_id
                        acknowledgement_of_receipt.created_by = user_name
                        acknowledgement_of_receipt.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('voluntary_self_identification_page7', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'acknowledgement_of_receipt_form': acknowledgement_of_receipt_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/page_six.html", context)

                elif request.method == 'POST':
                    acknowledgement_of_receipt = AcknowledgementOfReceipt.objects.get(employee_id=employee_id)
                    acknowledgement_of_receipt_form = AcknowledgementOfReceiptForm(
                        data=request.POST,
                        instance=acknowledgement_of_receipt)

                    if acknowledgement_of_receipt_form.is_valid():

                        acknowledgement_of_receipt = acknowledgement_of_receipt_form.save(commit=False)
                        acknowledgement_of_receipt.employee_id = employee_id
                        acknowledgement_of_receipt.updated_at = datetime.now()
                        acknowledgement_of_receipt.updated_by = user_name
                        acknowledgement_of_receipt.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('voluntary_self_identification_page7', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'acknowledgement_of_receipt_form': acknowledgement_of_receipt_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/page_six.html", context)
                else:
                    context = {
                        'employee_id': employee_id,
                        'acknowledgement_of_receipt_form': acknowledgement_of_receipt_form,
                    }
                    return render(request, "employee/page_six.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')


class VoluntarySelfIdentificationPage7(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_name:
                    user_role = Users.objects.get(employee_id=user_name)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                    else:
                        is_employee = user_role.is_employee

                if VoluntaryIdentification.objects.filter(employee_id=employee_id).exists():
                    voluntary_identification = VoluntaryIdentification.objects.get(employee_id=employee_id)
                    voluntary_identification_form = VoluntaryIdentificationForm(instance=voluntary_identification)

                    context = {
                        'employee_id': employee_id,
                        'voluntary_identification_form': voluntary_identification_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page7': 'active',
                        'is_pagination': is_pagination,
                    }

                    return render(request, "employee/voluntary_self_identification_page7.html", context)
                else:
                    voluntary_identification_form = VoluntaryIdentificationForm()

                    context = {
                        'employee_id': employee_id,
                        'voluntary_identification_form': voluntary_identification_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page7': 'active',
                        'is_pagination': is_pagination,
                    }
                    return render(request, "employee/voluntary_self_identification_page7.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):

        if request.session.get('employee'):
            user_name = request.session.get('employee')
            voluntary_identification_form = VoluntaryIdentificationForm(request.POST or None)
            if not VoluntaryIdentification.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and voluntary_identification_form.is_valid():
                    employee_id = employee_id
                    voluntary_identification = voluntary_identification_form.save(commit=False)
                    voluntary_identification.employee_id = employee_id
                    voluntary_identification.created_by = user_name
                    voluntary_identification.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('authorization_background_check_page8', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'voluntary_identification_form': voluntary_identification_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/voluntary_self_identification_page7.html", context)

            elif request.method == 'POST':
                voluntary_identification = VoluntaryIdentification.objects.get(employee_id=employee_id)
                voluntary_identification_form = VoluntaryIdentificationForm(
                    data=request.POST,
                    instance=voluntary_identification)

                if voluntary_identification_form.is_valid():
                    voluntary_identification = voluntary_identification_form.save(commit=False)
                    voluntary_identification.employee_id = employee_id
                    voluntary_identification.updated_at = datetime.now()
                    voluntary_identification.updated_by = user_name
                    voluntary_identification.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('authorization_background_check_page8', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'voluntary_identification_form': voluntary_identification_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/voluntary_self_identification_page7.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'voluntary_identification_form': voluntary_identification_form,
                }
                return render(request, "employee/voluntary_self_identification_page7.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')


class AuthorizationBackgroundCheckPage8(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_name:
                    user_role = Users.objects.get(employee_id=user_name)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                    else:
                        is_employee = user_role.is_employee
                if AuthorizationBackgroundCheck.objects.filter(employee_id=employee_id).exists():
                    authorization_background_check = AuthorizationBackgroundCheck.objects.get(employee_id=employee_id)
                    authorization_background_check_form = AuthorizationBackgroundCheckForm(
                        instance=authorization_background_check)

                    context = {
                        'employee_id': employee_id,
                        'authorization_background_check_form': authorization_background_check_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page8': 'active',
                        'is_pagination': is_pagination,
                    }

                    return render(request, "employee/authorization_background_check_page8.html", context)
                else:
                    authorization_background_check_form = AuthorizationBackgroundCheckForm()

                    context = {
                        'employee_id': employee_id,
                        'authorization_background_check_form': authorization_background_check_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page8': 'active',
                        'is_pagination': is_pagination,
                    }
                    return render(request, "employee/authorization_background_check_page8.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                authorization_background_check_form = AuthorizationBackgroundCheckForm(request.POST or None)
                if not AuthorizationBackgroundCheck.objects.filter(employee_id=employee_id).exists():
                    if request.method == "POST" and authorization_background_check_form.is_valid():
                        employee_id = employee_id
                        authorization_background_check = authorization_background_check_form.save(commit=False)
                        authorization_background_check.employee_id = employee_id
                        authorization_background_check.created_by = user_name
                        authorization_background_check.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('agreement_with_company_page9', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'authorization_background_check_form': authorization_background_check_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/authorization_background_check_page8.html", context)

                elif request.method == 'POST':
                    authorization_background_check = AuthorizationBackgroundCheck.objects.get(employee_id=employee_id)
                    authorization_background_check_form = AuthorizationBackgroundCheckForm(
                        data=request.POST,
                        instance=authorization_background_check)

                    if authorization_background_check_form.is_valid():
                        authorization_background_check = authorization_background_check_form.save(commit=False)
                        authorization_background_check.employee_id = employee_id
                        authorization_background_check.updated_at = datetime.now()
                        authorization_background_check.updated_by = user_name
                        authorization_background_check.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('agreement_with_company_page9', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'authorization_background_check_form': authorization_background_check_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/authorization_background_check_page8.html", context)
                else:
                    context = {
                        'employee_id': employee_id,
                        'authorization_background_check_form': authorization_background_check_form,
                    }

                    return render(request, "employee/authorization_background_check_page8.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')


class AgreementWithCompanyPage9(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_name:
                    user_role = Users.objects.get(employee_id=user_name)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                    else:
                        is_employee = user_role.is_employee
                if AgreementWithCompany.objects.filter(employee_id=employee_id).exists():
                    agreement_with_company = AgreementWithCompany.objects.get(employee_id=employee_id)
                    agreement_with_company_form = AgreementWithCompanyForm(
                        instance=agreement_with_company)

                    context = {
                        'employee_id': employee_id,
                        'agreement_with_company_form': agreement_with_company_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page9': 'active',
                        'is_pagination': is_pagination,
                    }

                    return render(request, "employee/agreement_with_company_page9.html", context)
                else:
                    agreement_with_company_form = AgreementWithCompanyForm()

                    context = {
                        'employee_id': employee_id,
                        'agreement_with_company_form': agreement_with_company_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'page9': 'active',
                        'is_pagination': is_pagination,
                    }
                    return render(request, "employee/agreement_with_company_page9.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                agreement_with_company_form = AgreementWithCompanyForm(request.POST or None)
                if not AgreementWithCompany.objects.filter(employee_id=employee_id).exists():
                    if request.method == "POST" and agreement_with_company_form.is_valid():
                        employee_id = employee_id
                        agreement_with_company = agreement_with_company_form.save(commit=False)
                        agreement_with_company.employee_id = employee_id
                        agreement_with_company.created_by = user_name
                        agreement_with_company.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('drug_and_alcohol_testing', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'agreement_with_company_form': agreement_with_company_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/agreement_with_company_page9.html", context)

                elif request.method == 'POST':
                    agreement_with_company = AgreementWithCompany.objects.get(employee_id=employee_id)
                    agreement_with_company_form = AgreementWithCompanyForm(
                        data=request.POST,
                        instance=agreement_with_company)

                    if agreement_with_company_form.is_valid():
                        agreement_with_company = agreement_with_company_form.save(commit=False)
                        agreement_with_company.employee_id = employee_id
                        agreement_with_company.updated_at = datetime.now()
                        agreement_with_company.updated_by = user_name
                        agreement_with_company.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('drug_and_alcohol_testing', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'agreement_with_company_form': agreement_with_company_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/agreement_with_company_page9.html", context)
                else:
                    context = {
                        'employee_id': employee_id,
                        'agreement_with_company_form': agreement_with_company_form,
                    }

                    return render(request, "employee/agreement_with_company_page9.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')


class DrugAndAlcoholTesting(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                is_admin = False
                is_super_admin = False
                is_employee = False
                is_pagination = False

                if DisclosureDrugTesting.objects.filter(employee_id=employee_id).exists():
                    is_pagination = True

                if user_name:
                    user_role = Users.objects.get(employee_id=user_name)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                    else:
                        is_employee = user_role.is_employee
                if DisclosureDrugTesting.objects.filter(employee_id=employee_id).exists():
                    disclosure_drug_testing = DisclosureDrugTesting.objects.get(employee_id=employee_id)
                    disclosure_drug_testing_form = DisclosureDrugTestingForm(
                        instance=disclosure_drug_testing)

                    context = {
                        'employee_id': employee_id,
                        'disclosure_drug_testing_form': disclosure_drug_testing_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'alcohol_testing': 'active',
                        'is_pagination': is_pagination,
                    }

                    return render(request, "employee/disclosure_drug_testing.html", context)
                else:
                    disclosure_drug_testing_form = DisclosureDrugTestingForm()

                    context = {
                        'employee_id': employee_id,
                        'disclosure_drug_testing_form': disclosure_drug_testing_form,
                        'is_admin': is_admin,
                        'is_super_admin': is_super_admin,
                        'is_employee': is_employee,
                        'alcohol_testing': 'active',
                        'is_pagination': is_pagination,
                    }
                    return render(request, "employee/disclosure_drug_testing.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:
            if request.session.get('employee'):
                user_name = request.session.get('employee')
                disclosure_drug_testing_form = DisclosureDrugTestingForm(request.POST or None)
                if not DisclosureDrugTesting.objects.filter(employee_id=employee_id).exists():
                    if request.method == "POST" and disclosure_drug_testing_form.is_valid():
                        employee_id = employee_id
                        disclosure_drug_testing = disclosure_drug_testing_form.save(commit=False)
                        disclosure_drug_testing.employee_id = employee_id
                        disclosure_drug_testing.created_by = user_name
                        disclosure_drug_testing.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('notice_acknowledgement_page10', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'disclosure_drug_testing_form': disclosure_drug_testing_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/disclosure_drug_testing.html", context)

                elif request.method == 'POST':
                    disclosure_drug_testing = DisclosureDrugTesting.objects.get(employee_id=employee_id)
                    disclosure_drug_testing_form = DisclosureDrugTestingForm(
                        data=request.POST,
                        instance=disclosure_drug_testing)

                    if disclosure_drug_testing_form.is_valid():
                        disclosure_drug_testing = disclosure_drug_testing_form.save(commit=False)
                        disclosure_drug_testing.employee_id = employee_id
                        disclosure_drug_testing.updated_at = datetime.now()
                        disclosure_drug_testing.updated_by = user_name
                        disclosure_drug_testing.save()

                        messages.success(request, 'Data Submission Successful!!')
                        return redirect('notice_acknowledgement_page10', employee_id)
                    else:
                        context = {
                            'employee_id': employee_id,
                            'disclosure_drug_testing_form': disclosure_drug_testing_form,
                        }
                        messages.error(request, 'Data Submission Failed!!')
                        return render(request, "employee/disclosure_drug_testing.html", context)
                else:
                    context = {
                        'employee_id': employee_id,
                        'disclosure_drug_testing_form': disclosure_drug_testing_form,
                    }

                    return render(request, "employee/disclosure_drug_testing.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')


class NoticeAcknowledgementPage10(View):
    @staticmethod
    def get(request, employee_id):
        if request.session.get('employee'):
            user_name = request.session.get('employee')
            is_admin = False
            is_super_admin = False
            is_employee = False
            is_pagination = False

            if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                is_pagination = True

            if user_name:
                user_role = Users.objects.get(employee_id=user_name)
                if user_role.is_admin:
                    is_admin = user_role.is_admin
                elif user_role.is_super_admin:
                    is_super_admin = user_role.is_super_admin
                else:
                    is_employee = user_role.is_employee
            if EmployerInformation.objects.filter(employee_id=employee_id).exists() \
                    and NoticeAcknowledgement.objects.filter(employee_id=employee_id).exists():
                employer_information = EmployerInformation.objects.get(employee_id=employee_id)
                notice_acknowledgement = NoticeAcknowledgement.objects.get(employee_id=employee_id)

                employer_information_form = EmployerInformationForm(instance=employer_information)
                notice_acknowledgement_form = NoticeAcknowledgementForm(instance=notice_acknowledgement)

                context = {
                    'employee_id': employee_id,
                    'employer_information_form': employer_information_form,
                    'notice_acknowledgement_form': notice_acknowledgement_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page10': 'active',
                    'is_pagination': is_pagination,
                }

                return render(request, "employee/notice_acknowledgement_page10.html", context)
            else:
                employer_information_form = EmployerInformationForm(
                    initial={
                        'name': 'BARI HOME CARE LLC',
                        'physical_address': '469 Donald Blvd, Holbrook, NY 11741',
                        'mail_address': '469 Donald Blvd, Holbrook, NY 11741',
                        'phone': '718 - 898 - 7100',
                    }
                )
                notice_acknowledgement_form = NoticeAcknowledgementForm()

                context = {
                    'employee_id': employee_id,
                    'employer_information_form': employer_information_form,
                    'notice_acknowledgement_form': notice_acknowledgement_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page10': 'active',
                    'is_pagination': is_pagination,
                }
                return render(request, "employee/notice_acknowledgement_page10.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        if request.session.get('employee'):
            user_name = request.session.get('employee')
            employer_information_form = EmployerInformationForm(request.POST or None)
            notice_acknowledgement_form = NoticeAcknowledgementForm(request.POST or None)
            if not EmployerInformation.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and employer_information_form.is_valid() \
                        and notice_acknowledgement_form.is_valid():

                    employee_id = employee_id
                    employer_information = employer_information_form.save(commit=False)
                    employer_information.employee_id = employee_id
                    employer_information.created_by = user_name
                    employer_information.save()

                    employee_id = employee_id
                    notice_acknowledgement = notice_acknowledgement_form.save(commit=False)
                    notice_acknowledgement.employee_id = employee_id
                    notice_acknowledgement.created_by = user_name
                    notice_acknowledgement.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('benefit_portion_compensation_page11', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employer_information_form': employer_information_form,
                        'notice_acknowledgement_form': notice_acknowledgement_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/notice_acknowledgement_page10.html", context)

            elif request.method == 'POST':
                employer_information = EmployerInformation.objects.get(employee_id=employee_id)
                notice_acknowledgement = NoticeAcknowledgement.objects.get(employee_id=employee_id)

                employer_information_form = EmployerInformationForm(data=request.POST,
                                                                    instance=employer_information)

                notice_acknowledgement_form = NoticeAcknowledgementForm(data=request.POST,
                                                                        instance=notice_acknowledgement)

                if employer_information_form.is_valid() and notice_acknowledgement_form.is_valid():

                    employer_information = employer_information_form.save(commit=False)
                    employer_information.employee_id = employee_id
                    employer_information.updated_at = datetime.now()
                    employer_information.updated_by = user_name
                    employer_information.save()

                    notice_acknowledgement = notice_acknowledgement_form.save(commit=False)
                    notice_acknowledgement.employee_id = employee_id
                    notice_acknowledgement.updated_at = datetime.now()
                    notice_acknowledgement.updated_by = user_name
                    notice_acknowledgement.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('benefit_portion_compensation_page11', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employer_information_form': employer_information_form,
                        'notice_acknowledgement_form': notice_acknowledgement_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/notice_acknowledgement_page10.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'employer_information_form': employer_information_form,
                    'notice_acknowledgement_form': notice_acknowledgement_form,
                }

                return render(request, "employee/notice_acknowledgement_page10.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')


class BenefitPortionCompensationPage11(View):
    @staticmethod
    def get(request, employee_id):

        if request.session.get('employee'):
            user_name = request.session.get('employee')
            is_admin = False
            is_super_admin = False
            is_employee = False
            is_pagination = False

            if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                is_pagination = True

            if user_name:
                user_role = Users.objects.get(employee_id=user_name)
                if user_role.is_admin:
                    is_admin = user_role.is_admin
                elif user_role.is_super_admin:
                    is_super_admin = user_role.is_super_admin
                else:
                    is_employee = user_role.is_employee

            if BenefitPortionCompensation.objects.filter(employee_id=employee_id).exists() \
                    and EmployeeAcknowledgement.objects.filter(employee_id=employee_id).exists():
                benefit_portion_compensation = BenefitPortionCompensation.objects.get(employee_id=employee_id)
                employee_acknowledgement = EmployeeAcknowledgement.objects.get(employee_id=employee_id)
                benefit_portion_compensation_form = BenefitPortionCompensationForm(
                    instance=benefit_portion_compensation)
                employee_acknowledgement_form = EmployeeAcknowledgementForm(
                    instance=employee_acknowledgement)

                context = {
                    'employee_id': employee_id,
                    'benefit_portion_compensation_form': benefit_portion_compensation_form,
                    'employee_acknowledgement_form': employee_acknowledgement_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page11': 'active',
                    'is_pagination': is_pagination,
                }

                return render(request, "employee/benefit_portion_compensation_page11.html", context)
            else:
                benefit_portion_compensation_form = BenefitPortionCompensationForm()
                employee_acknowledgement_form = EmployeeAcknowledgementForm(
                    initial={
                        'primary_language': 'English',
                    }
                )

                context = {
                    'employee_id': employee_id,
                    'benefit_portion_compensation_form': benefit_portion_compensation_form,
                    'employee_acknowledgement_form': employee_acknowledgement_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page11': 'active',
                    'is_pagination': is_pagination,
                }
                return render(request, "employee/benefit_portion_compensation_page11.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')

    @staticmethod
    def post(request, employee_id):

        if request.session.get('employee'):
            user_name = request.session.get('employee')
            benefit_portion_compensation_form = BenefitPortionCompensationForm(request.POST or None)
            employee_acknowledgement_form = EmployeeAcknowledgementForm(request.POST or None)

            if not BenefitPortionCompensation.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and benefit_portion_compensation_form.is_valid() \
                        and employee_acknowledgement_form.is_valid():

                    employee_id = employee_id
                    benefit_portion_compensation = benefit_portion_compensation_form.save(commit=False)
                    benefit_portion_compensation.employee_id = employee_id
                    benefit_portion_compensation.created_by = user_name
                    benefit_portion_compensation.save()

                    employee_acknowledgement = employee_acknowledgement_form.save(commit=False)
                    employee_acknowledgement.employee_id = employee_id
                    employee_acknowledgement.created_by = user_name
                    employee_acknowledgement.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('deposit_authorization_page12', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'benefit_portion_compensation_form': benefit_portion_compensation_form,
                        'employee_acknowledgement_form': employee_acknowledgement_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/benefit_portion_compensation_page11.html", context)

            elif request.method == 'POST':
                benefit_portion_compensation = BenefitPortionCompensation.objects.get(employee_id=employee_id)
                employee_acknowledgement = EmployeeAcknowledgement.objects.get(employee_id=employee_id)

                benefit_portion_compensation_form = BenefitPortionCompensationForm(
                    data=request.POST,
                    instance=benefit_portion_compensation)

                employee_acknowledgement_form = EmployeeAcknowledgementForm(
                    data=request.POST,
                    instance=employee_acknowledgement)

                if benefit_portion_compensation_form.is_valid() and employee_acknowledgement_form.is_valid():

                    benefit_portion_compensation = benefit_portion_compensation_form.save(commit=False)
                    benefit_portion_compensation.employee_id = employee_id
                    benefit_portion_compensation.updated_at = datetime.now()
                    benefit_portion_compensation.updated_by = user_name
                    benefit_portion_compensation.save()

                    employee_acknowledgement = employee_acknowledgement_form.save(commit=False)
                    employee_acknowledgement.employee_id = employee_id
                    employee_acknowledgement.updated_at = datetime.now()
                    employee_acknowledgement.updated_by = user_name
                    employee_acknowledgement.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('deposit_authorization_page12', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'benefit_portion_compensation_form': benefit_portion_compensation_form,
                        'employee_acknowledgement_form': employee_acknowledgement_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/benefit_portion_compensation_page11.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'benefit_portion_compensation_form': benefit_portion_compensation_form,
                    'employee_acknowledgement_form': employee_acknowledgement_form,
                }

                return render(request, "employee/benefit_portion_compensation_page11.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')


class DepositAuthorizationPage12(View):
    @staticmethod
    def get(request, employee_id):
        if request.session.get('employee'):
            user_name = request.session.get('employee')
            is_admin = False
            is_super_admin = False
            is_employee = False
            is_pagination = False

            if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                is_pagination = True

            if user_name:
                user_role = Users.objects.get(employee_id=user_name)
                if user_role.is_admin:
                    is_admin = user_role.is_admin
                elif user_role.is_super_admin:
                    is_super_admin = user_role.is_super_admin
                else:
                    is_employee = user_role.is_employee
            if DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                deposit_authorization = DepositAuthorization.objects.get(employee_id=employee_id)
                deposit_authorization_form = DepositAuthorizationForm(
                    instance=deposit_authorization)

                context = {
                    'employee_id': employee_id,
                    'deposit_authorization_form': deposit_authorization_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page12': 'active',
                    'is_pagination': is_pagination,
                }

                return render(request, "employee/deposit_authorization_page12.html", context)
            else:
                deposit_authorization_form = DepositAuthorizationForm()

                context = {
                    'employee_id': employee_id,
                    'deposit_authorization_form': deposit_authorization_form,
                    'is_admin': is_admin,
                    'is_super_admin': is_super_admin,
                    'is_employee': is_employee,
                    'page12': 'active',
                    'is_pagination': is_pagination,
                }
                return render(request, "employee/deposit_authorization_page12.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        if request.session.get('employee'):
            user_name = request.session.get('employee')
            deposit_authorization_form = DepositAuthorizationForm(request.POST or None)

            if not DepositAuthorization.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and deposit_authorization_form.is_valid():
                    employee_id = employee_id
                    deposit_authorization = deposit_authorization_form.save(commit=False)
                    deposit_authorization.employee_id = employee_id
                    deposit_authorization.created_by = user_name
                    deposit_authorization.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('deposit_authorization_page12', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'deposit_authorization_form': deposit_authorization_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/deposit_authorization_page12.html", context)

            elif request.method == 'POST':
                deposit_authorization = DepositAuthorization.objects.get(employee_id=employee_id)
                deposit_authorization_form = DepositAuthorizationForm(
                    data=request.POST,
                    instance=deposit_authorization)

                if deposit_authorization_form.is_valid():
                    deposit_authorization = deposit_authorization_form.save(commit=False)
                    deposit_authorization.employee_id = employee_id
                    deposit_authorization.updated_at = datetime.now()
                    deposit_authorization.updated_by = user_name
                    deposit_authorization.save()

                    messages.success(request, 'Data Submission Successful!!')
                    return redirect('deposit_authorization_page12', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'deposit_authorization_form': deposit_authorization_form,
                    }
                    messages.error(request, 'Data Submission Failed!!')
                    return render(request, "employee/deposit_authorization_page12.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'deposit_authorization_form': deposit_authorization_form,
                }

                return render(request, "employee/deposit_authorization_page12.html", context)
        else:
            messages.error(request, 'Session Expired!!')
            return redirect('login')


""" Logout View """


class LogoutView(View):

    @staticmethod
    def get(request):
        try:
            request.session.flush()
            return redirect('login')
        except Exception as e:
            print(e)
            return render(request, 'employee/log-in.html', )
