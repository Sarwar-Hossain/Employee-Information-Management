from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib import messages
from admin_app.forms import *
from employee_app.forms import EmployeeForm

""" Admin Login View """


class AdminLoginView(View):

    @staticmethod
    def get(request):
        try:
            return render(request, 'admin/log-in.html')
        except Exception as e:
            print(e)
            return render(request, 'admin/log-in.html', )

    @staticmethod
    def post(request):
        try:
            employee_id = 1
            email = request.POST.get('email')
            password = request.POST.get('password')
            # user = Employee.objects.get(email=email)
            if email == 'admin@gmail.com':
                messages.success(request, 'Login Successful!!')
                return redirect("create_employee_user")
            else:
                return redirect("index", employee_id)

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
            return render(request, 'admin/log-in.html', )


class CreateEmployeeUser(View):

    @staticmethod
    def get(request):
        try:
            user_form = UserForm()

            context = {
                'user_form': user_form,
            }

            return render(request, "admin/user-form.html", context)
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request):
        try:

            user_form = UserForm(request.POST or None)
            # employee_form = EmployeeForm()

            if request.method == "POST" and user_form.is_valid():
                user_form.save()
                # employee_form.save()

                return redirect('create_employee_user')
            context = {
                'user_form': user_form,
            }
            return render(request, "admin/user-form.html", context)
        except Exception as e:
            print(e)
            return redirect('login')


""" Logout View """


class AdminLogoutView(View):

    @staticmethod
    def get(request):
        try:
            request.session.flush()
            return redirect('login')
        except Exception as e:
            print(e)
            return render(request, 'admin/log-in.html', )
