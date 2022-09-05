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
                        if user.is_admin is True:
                            if user.is_active:
                                request.session['user_name'] = user.employee_name
                                messages.success(request, 'Login Successful!')
                                return redirect("create_employee_user")
                            else:
                                messages.error(request, 'User is not Active!!')
                                return redirect("login")
                        else:
                            messages.error(request, 'User is not Admin!!')
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
                            request.session['user_name'] = user.employee_name
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

            user = Users.objects.get(employee_id=employee_id)
            user_form = EmployeeForm(readonly_form=True, initial={
                'employee_name': user.employee_name,
                'date_of_service': user.date_of_service,
                'medicaid_id': user.medicaid_id,
                'pa_name': user.pa_name,
                'employee_id': user.employee_id,
                'mobile_no': user.mobile_no,
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
                    }
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
                    }
                    return render(request, "employee/index.html", context)
            elif Transportation.objects.filter(employee_id=employee_id).exists():
                user = Users.objects.get(employee_id=employee_id)
                demographics = Demographics.objects.get(employee_id=employee_id)
                hours_available = HoursAvailable.objects.get(employee_id=employee_id)
                education = Education.objects.get(employee_id=employee_id)
                training = ProfessionalTraining.objects.get(employee_id=employee_id)
                skills = SkillsChecklist.objects.get(employee_id=employee_id)
                transportation = Transportation.objects.get(employee_id=employee_id)

                if user and demographics and hours_available and education and training and skills and transportation:
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
                    }
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
                    }
                    return render(request, "employee/index.html", context)
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:
            employee_id = employee_id
            # user_form = EmployeeForm(request.POST or None)
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
                demographics_form.save()

                # hours_available_form
                hours_available_form = hours_available_form.save(commit=False)
                hours_available_form.employee_id = employee_id
                hours_available_form.save()

                # education_form
                education_form = education_form.save(commit=False)
                education_form.employee_id = employee_id
                education_form.save()

                # training_form
                training_form = training_form.save(commit=False)
                training_form.employee_id = employee_id
                training_form.save()

                # training_form
                skills_form = skills_form.save(commit=False)
                skills_form.employee_id = employee_id
                skills_form.save()

                # transportation_form
                transportation_form = transportation_form.save(commit=False)
                transportation_form.employee_id = employee_id
                transportation_form.save()

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
                        hours_available = demographics_form.save(commit=False)
                        hours_available.employee_id = employee_id
                        hours_available.updated_at = datetime.now()
                        hours_available.save()

                        education = Education.objects.get(employee_id=employee_id)
                        education_form = EducationForm(data=request.POST, instance=education)
                        if education_form.is_valid():
                            education = education_form.save(commit=False)
                            education.employee_id = employee_id
                            education.updated_at = datetime.now()
                            education.save()

                            training = ProfessionalTraining.objects.get(employee_id=employee_id)
                            training_form = ProfessionalTrainingForm(data=request.POST, instance=training)
                            if training_form.is_valid():
                                training = training_form.save(commit=False)
                                training.employee_id = employee_id
                                training.updated_at = datetime.now()
                                training.save()

                                skills = SkillsChecklist.objects.get(employee_id=employee_id)
                                skills_form = SkillsChecklistForm(data=request.POST, instance=skills)
                                if skills_form.is_valid():
                                    skills = skills_form.save(commit=False)
                                    skills.employee_id = employee_id
                                    skills.updated_at = datetime.now()
                                    skills.save()

                                    transportation = Transportation.objects.get(employee_id=employee_id)
                                    transportation_form = TransportationForm(data=request.POST,
                                                                             instance=transportation)
                                    if transportation_form.is_valid():
                                        transportation = transportation_form.save(commit=False)
                                        transportation.employee_id = employee_id
                                        transportation.updated_at = datetime.now()
                                        transportation.save()
                                        return redirect('section_w4', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        # 'user_form': user_form,
                        'demographics_form': demographics_form,
                        'hours_available_form': hours_available_form,
                        'education_form': education_form,
                        'training_form': training_form,
                        'skills_form': skills_form,
                        'transportation_form': transportation_form,
                    }
                    return render(request, "employee/index.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    # 'user_form': user_form,
                    'demographics_form': demographics_form,
                    'hours_available_form': hours_available_form,
                    'education_form': education_form,
                    'training_form': training_form,
                    'skills_form': skills_form,
                    'transportation_form': transportation_form,
                }
                return render(request, "employee/index.html", context)
        except Exception as e:
            print(e)
            return redirect('login')


class CreateEmployeeProfileW4(View):
    @staticmethod
    def get(request, employee_id):
        try:
            if EmployeeWithholdingCertificate.objects.filter(employee_id=employee_id).exists():
                demographics = Demographics.objects.get(employee_id=employee_id)
                employee_withholding_certificate = EmployeeWithholdingCertificate.objects.get(employee_id=employee_id)
                withholding_certificate_form = EmployeeWithholdingCertificateForm(
                    instance=employee_withholding_certificate,
                    initial={
                        'last_name': demographics.last_name,
                        'social_security_number': demographics.social_security_number
                    })

                context = {
                    'employee_id': employee_id,
                    'withholding_certificate_form': withholding_certificate_form,
                }

                return render(request, "employee/section_w4.html", context)
            else:

                demographics = Demographics.objects.get(employee_id=employee_id)
                withholding_certificate_form = EmployeeWithholdingCertificateForm(initial={
                    'last_name': demographics.last_name,
                    'social_security_number': demographics.social_security_number
                })

                # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                context = {
                    'employee_id': employee_id,
                    'withholding_certificate_form': withholding_certificate_form,
                }

                return render(request, "employee/section_w4.html", context)
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:

            withholding_certificate_form = EmployeeWithholdingCertificateForm(request.POST or None)
            if not EmployeeWithholdingCertificate.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and withholding_certificate_form.is_valid():
                    employee_id = employee_id

                    # demographics_form
                    withholding_certificate = withholding_certificate_form.save(commit=False)
                    withholding_certificate.employee_id = employee_id
                    withholding_certificate_form.save()

                    return redirect('allowance_certificate', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'withholding_certificate_form': withholding_certificate_form,
                    }
                    return render(request, "employee/section_w4.html", context)

            elif request.method == 'POST':
                withholding_certificate = EmployeeWithholdingCertificate.objects.get(employee_id=employee_id)
                withholding_certificate_form = EmployeeWithholdingCertificateForm(data=request.POST,
                                                                                  instance=withholding_certificate)
                if withholding_certificate_form.is_valid():
                    withholding_certificate = withholding_certificate_form.save(commit=False)
                    withholding_certificate.employee_id = employee_id
                    withholding_certificate.updated_at = datetime.now()
                    withholding_certificate.save()
                    return redirect('allowance_certificate', employee_id)
            else:
                context = {
                    'employee_id': employee_id,
                    'withholding_certificate_form': withholding_certificate_form,
                }
                return render(request, "employee/section_w4.html", context)
        except Exception as e:
            print(e)
            return redirect('login')


class UpdateEmployeeProfile(View):

    @staticmethod
    def get(request):
        try:
            user = DemoUser.objects.get(id=1)
            form = DemoUserForm(instance=user)

            # form = EmployeeForm(request.POST or None)
            context = {'form': form}
            return render(request, "employee/name.html", context)
            # messages.success(request, 'Login Successful!!')
            # return render(request, 'index.html')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request):
        try:
            form = DemoUserForm(request.POST or None)
            if request.method == "POST" and form.is_valid():
                signature = form.cleaned_data.get('signature')
                name = request.POST.get('name')
                form.save()
                return HttpResponse('POST')
        except Exception as e:
            print(e)
            return redirect('login')


class CreateEmployeeAllowanceCertificate(View):
    @staticmethod
    def get(request, employee_id):
        try:
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
                }

                return render(request, "employee/allowance_certificate.html", context)
            else:

                demographics = Demographics.objects.get(employee_id=employee_id)
                employee_withholding_certificate = EmployeeWithholdingCertificate.objects.get(
                    employee_id=employee_id)
                employee_withholding_allowance_certificate_form = EmployeeWithholdingAllowanceCertificateForm(initial={
                    'last_name': demographics.last_name,
                    'social_security_number': demographics.social_security_number,
                    'zip_code': demographics.state_zip_code,
                    'employer_identification_no': employee_withholding_certificate.employer_identification_no,
                })

                # withholding_certificate_form = EmployeeWithholdingCertificateForm()
                context = {
                    'employee_id': employee_id,
                    'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                }

                return render(request, "employee/allowance_certificate.html", context)
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request, employee_id):
        try:

            employee_withholding_allowance_certificate_form = EmployeeWithholdingAllowanceCertificateForm(
                request.POST or None)
            if not EmployeeWithholdingAllowanceCertificate.objects.filter(employee_id=employee_id).exists():
                if request.method == "POST" and employee_withholding_allowance_certificate_form.is_valid():
                    employee_id = employee_id

                    # demographics_form
                    withholding_allowance_certificate = employee_withholding_allowance_certificate_form.save(
                        commit=False)
                    withholding_allowance_certificate.employee_id = employee_id
                    employee_withholding_allowance_certificate_form.save()

                    return redirect('allowance_certificate', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                    }
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
                    allowance_certificate.updated_at = datetime.now()
                    allowance_certificate.save()
                    return redirect('allowance_certificate', employee_id)
                else:
                    context = {
                        'employee_id': employee_id,
                        'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                    }
                    return render(request, "employee/allowance_certificate.html", context)
            else:
                context = {
                    'employee_id': employee_id,
                    'employee_withholding_allowance_certificate_form': employee_withholding_allowance_certificate_form,
                }
                return render(request, "employee/allowance_certificate.html", context)
        except Exception as e:
            print(e)
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
