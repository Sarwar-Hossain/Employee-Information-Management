from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import *
from django.contrib import messages
from employee_app.forms import *
from jsignature.utils import draw_signature

""" Login View """


class LoginView(View):

    @staticmethod
    def get(request):
        try:
            return redirect(request, 'log-in.html')
        except Exception as e:
            print(e)
            return render(request, 'log-in.html', )

    @staticmethod
    def post(request):
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            # user = Employee.objects.get(email=email)
            messages.success(request, 'Login Successful!!')
            return HttpResponseRedirect("index")

            # if user is not None:
            #     if user.is_active:
            #         # login(request, user)
            #         messages.success(request, 'Login Successful!!')
            #         return redirect("index")
            #     else:
            #         messages.success(request, 'User in not Active!!')
            #         return redirect("login")
            # else:
            #     return redirect('login')
        except Exception as e:
            print(e)
            return render(request, 'log-in.html', )


class CreateEmployeeProfile(View):

    @staticmethod
    def get(request):
        try:
            form = EmployeeForm()
            demographics_form = DemographicsForm()
            hours_available_form = HoursAvailableForm()
            education_form = EducationForm()
            # form = EmployeeForm(request.POST or None)
            context = {
                'form': form,
                'demographics_form': demographics_form,
                'hours_available_form': hours_available_form,
                'education_form': education_form,
            }
            return render(request, "index.html", context)
            # messages.success(request, 'Login Successful!!')
            # return render(request, 'index.html')
        except Exception as e:
            print(e)
            return render(request, 'log-in.html', )

    @staticmethod
    def post(request):
        try:
            form = EmployeeForm(request.POST or None)
            demographics_form = DemographicsForm(request.POST or None)
            hours_available_form = HoursAvailableForm(request.POST or None)
            education_form = EducationForm(request.POST or None)

            if request.method == "POST" and demographics_form.is_valid() and form.is_valid()\
                    and hours_available_form.is_valid() and education_form.is_valid():

                employee_id = form.cleaned_data.get('employee_id')
                # name = request.POST.get('name')
                form.save()

                # demographics_form
                demographics = demographics_form.save(commit=False)
                demographics.employee_id = employee_id
                # obj.save()
                demographics_form.save()

                # hours_available_form
                hours_available_form = hours_available_form.save(commit=False)
                hours_available_form.employee_id = employee_id
                hours_available_form.save()

                # education_form
                education_form = education_form.save(commit=False)
                education_form.employee_id = employee_id
                education_form.save()

                return redirect('index')
            context = {
                'form': form,
                'demographics_form': demographics_form,
                'hours_available_form': hours_available_form,
                'education_form': education_form,
            }
            return render(request, "index.html", context)
        except Exception as e:
            print(e)
            return render(request, 'log-in.html', )


class UpdateEmployeeProfile(View):

    @staticmethod
    def get(request):
        try:
            user = DemoUser.objects.get(id=1)
            form = DemoUserForm(instance=user)

            # form = EmployeeForm(request.POST or None)
            context = {'form': form}
            return render(request, "name.html", context)
            # messages.success(request, 'Login Successful!!')
            # return render(request, 'index.html')
        except Exception as e:
            print(e)
            return render(request, 'log-in.html', )

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
            return render(request, 'log-in.html', )


""" Logout View """


class LogoutView(View):

    @staticmethod
    def get(request):
        try:
            request.session.flush()
            return redirect('login')
        except Exception as e:
            print(e)
            return render(request, 'log-in.html', )
