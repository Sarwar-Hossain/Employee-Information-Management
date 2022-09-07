from django.forms import modelform_factory
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from admin_app.forms import *
from employee_app.forms import EmployeeForm
import datetime
from datetime import datetime
from admin_app.aes_cipher import AESCipher

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
                return redirect("create_employee_user_super_admin")
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


class CreateUserSuperAdmin(View):

    @staticmethod
    def get(request):
        try:
            user_form = UserForm()
            shop_users = Users.objects.all().order_by('employee_name')

            context = {
                'user_form': user_form,
                'shop_users': shop_users,
            }

            return render(request, "admin/super_admin_user-form.html", context)
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request):
        try:
            shop_users = Users.objects.all().order_by('employee_name')
            employee_id = request.POST.get('button_select')
            if request.method == "POST" and request.POST.get('button_select'):
                user = Users.objects.get(employee_id=employee_id)
                decoded_pass = eval(user.password)
                password = AESCipher().decrypt(decoded_pass)
                user_form = UserForm(instance=user, initial={'password': password})
                context = {
                    'shop_users': shop_users,
                    'user_form': user_form,
                    'single_user': user,
                }
                messages.success(request, 'User Selected!!')
                return render(request, "admin/super_admin_user-form.html", context)

            elif request.method == "POST" and request.POST.get('user_deactivate'):

                user_deactivate_id = request.POST.get('user_deactivate')
                Users.objects.filter(employee_id=user_deactivate_id).update(is_active=False, )
                messages.success(request, 'User Deactivate Successfully!!')
                return redirect('create_employee_user_super_admin')

            elif request.method == "POST" and request.POST.get('user_activate'):

                user_activate_id = request.POST.get('user_activate')
                Users.objects.filter(employee_id=user_activate_id).update(is_active=True, )
                messages.success(request, 'User Activate Successfully!!')
                return redirect('create_employee_user_super_admin')

            elif request.method == "POST" and request.POST.get('button_update'):
                user_name = request.session.get('user_name')
                update_user_id = request.POST.get('button_update')
                user = Users.objects.get(employee_id=update_user_id)
                user_form = UserForm(data=request.POST, instance=user)
                if user_form.is_valid():
                    password = user_form.cleaned_data.get('password')
                    user = user_form.save(commit=False)
                    user.updated_at = datetime.now()
                    user.updated_by = user_name
                    user.password = AESCipher().encrypt(password)
                    user.save()
                    messages.success(request, 'User Updated Successfully!!')
                    return redirect('create_employee_user_super_admin')

            else:
                user_form = UserForm(request.POST or None)
                user_name = request.session.get('user_name')
                if request.method == "POST" and user_form.is_valid():
                    password = user_form.cleaned_data.get('password')
                    user_form = user_form.save(commit=False)
                    user_form.created_by = user_name
                    user_form.password = AESCipher().encrypt(password)
                    user_form.save()
                    messages.success(request, 'User Created Successfully!!')
                    return redirect('create_employee_user_super_admin')
                context = {
                    'shop_users': shop_users,
                    'user_form': user_form,
                }
                return render(request, "admin/super_admin_user-form.html", context)
        except Exception as e:
            print(e)
            return redirect('login')


class CreateUserAdmin(View):

    @staticmethod
    def get(request):
        try:
            user_name = request.session.get('user_name')
            user_form = UserForm()
            shop_users = Users.objects.filter(created_by=user_name).order_by('employee_name')

            context = {
                'user_form': user_form,
                'shop_users': shop_users,
            }

            return render(request, "admin/super_admin_user-form.html", context)
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request):
        try:
            user_name = request.session.get('user_name')
            shop_users = Users.objects.filter(created_by=user_name).order_by('employee_name')
            employee_id = request.POST.get('button_select')
            if request.method == "POST" and request.POST.get('button_select'):
                user = Users.objects.get(employee_id=employee_id)
                decoded_pass = eval(user.password)
                password = AESCipher().decrypt(decoded_pass)
                user_form = UserForm(instance=user, initial={'password': password})
                context = {
                    'shop_users': shop_users,
                    'user_form': user_form,
                    'single_user': user,
                }
                messages.success(request, 'User Selected!!')
                return render(request, "admin/admin_user_form.html", context)

            elif request.method == "POST" and request.POST.get('user_deactivate'):

                user_deactivate_id = request.POST.get('user_deactivate')
                Users.objects.filter(employee_id=user_deactivate_id).update(is_active=False, )
                messages.success(request, 'User Deactivate Successfully!!')
                return redirect('create_employee_user_admin')

            elif request.method == "POST" and request.POST.get('user_activate'):

                user_activate_id = request.POST.get('user_activate')
                Users.objects.filter(employee_id=user_activate_id).update(is_active=True, )
                messages.success(request, 'User Activate Successfully!!')
                return redirect('create_employee_user_admin')

            elif request.method == "POST" and request.POST.get('button_update'):
                user_name = request.session.get('user_name')
                update_user_id = request.POST.get('button_update')
                user = Users.objects.get(employee_id=update_user_id)
                user_form = UserForm(data=request.POST, instance=user)
                if user_form.is_valid():
                    password = user_form.cleaned_data.get('password')
                    user = user_form.save(commit=False)
                    user.updated_at = datetime.now()
                    user.updated_by = user_name
                    user.password = AESCipher().encrypt(password)
                    user.save()
                    messages.success(request, 'User Updated Successfully!!')
                    return redirect('create_employee_user_admin')

            else:
                user_form = UserForm(request.POST or None)
                user_name = request.session.get('user_name')

                if request.method == "POST" and user_form.is_valid():
                    password = user_form.cleaned_data.get('password')
                    user_form = user_form.save(commit=False)
                    user_form.created_by = user_name
                    user_form.password = AESCipher().encrypt(password)
                    user_form.save()
                    messages.success(request, 'User Created Successfully!!')
                    return redirect('create_employee_user_admin')
                context = {
                    'shop_users': shop_users,
                    'user_form': user_form,
                }
                return render(request, "admin/admin_user_form.html", context)
        except Exception as e:
            print(e)
            return redirect('login')


class DeleteUser(View):

    @staticmethod
    def get(request):
        try:
            user_id = request.GET.get('user_id')
            user_deleted = Users.objects.filter(employee_id=user_id).delete()

            context = {
                'toast_type': 'info',
                'toast_message': 'User Deleted Successfully!!',
            }
            return JsonResponse(context)
        finally:
            context = {
                'toast_type': 'error',
                'toast_message': 'User Could not be Deleted!!',
            }
            return JsonResponse(context)

    @staticmethod
    def post(request):
        try:
            # user_id = request.GET.get('user_id')
            # user_deleted = Users.objects.filter(id=user_id).delete()

            context = {
                'toast_type': 'info',
                'toast_message': 'User Deleted Successfully!!',
            }
            return JsonResponse(context)
        finally:
            context = {
                'toast_type': 'error',
                'toast_message': 'User Could not be Deleted!!',
            }
            return JsonResponse(context)


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
