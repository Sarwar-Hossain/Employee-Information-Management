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
from employment.settings import MEDIA_URL, MEDIA_ROOT

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
            if request.session.get('super_admin'):
                user_name = request.session.get('super_admin')
                user_form = UserForm()
                shop_users = Users.objects.all().order_by('employee_name')

                context = {
                    'user_form': user_form,
                    'shop_users': shop_users,
                }

                return render(request, "admin/super_admin_user-form.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request):
        try:
            if request.session.get('super_admin'):
                user_name = request.session.get('super_admin')
                shop_users = Users.objects.all().order_by('employee_name')
                employee_id = request.POST.get('button_select')
                if request.method == "POST" and request.POST.get('button_select'):
                    user = Users.objects.get(employee_id=employee_id)
                    decoded_pass = eval(user.password)
                    password = AESCipher().decrypt(decoded_pass)

                    if user.is_admin is True:
                        user_form = UserForm(instance=user, initial={'password': password, 'user_role': 'admin'})
                        context = {
                            'shop_users': shop_users,
                            'user_form': user_form,
                            'single_user': user,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
                        }
                        messages.success(request, 'User Selected!!')
                        return render(request, "admin/super_admin_user-form.html", context)
                    else:
                        user_form = UserForm(instance=user, initial={'password': password, 'user_role': 'employee'})
                        context = {
                            'shop_users': shop_users,
                            'user_form': user_form,
                            'single_user': user,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
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
                    user_name = request.session.get('super_admin')
                    update_user_id = request.POST.get('button_update')
                    user = Users.objects.get(employee_id=update_user_id)
                    user_form = UserForm(request.POST, request.FILES, instance=user)
                    if user_form.is_valid():
                        user_role = user_form.cleaned_data.get('user_role')
                        if user_role == 'employee':
                            password = user_form.cleaned_data.get('password')
                            user = user_form.save(commit=False)
                            user.updated_at = datetime.now()
                            user.is_employee = True
                            user.updated_by = user_name
                            user.password = AESCipher().encrypt(password)
                            user.save()
                            messages.success(request, 'User Updated Successfully!!')
                            return redirect('create_employee_user_super_admin')
                        else:
                            password = user_form.cleaned_data.get('password')
                            user = user_form.save(commit=False)
                            user.updated_at = datetime.now()
                            user.is_admin = True
                            user.updated_by = user_name
                            user.password = AESCipher().encrypt(password)
                            user.save()
                            messages.success(request, 'User Updated Successfully!!')
                            return redirect('create_employee_user_super_admin')
                    else:
                        return redirect('create_employee_user_super_admin')

                else:
                    user_form = UserForm(request.POST or None, request.FILES)
                    user_name = request.session.get('super_admin')
                    if request.method == "POST" and user_form.is_valid():
                        user_role = user_form.cleaned_data.get('user_role')
                        if user_role == 'admin':
                            password = user_form.cleaned_data.get('password')
                            user_form = user_form.save(commit=False)
                            user_form.is_admin = True
                            user_form.is_employee = True
                            user_form.created_by = user_name
                            user_form.password = AESCipher().encrypt(password)
                            user_form.save()
                            messages.success(request, 'Admin User Created Successfully!!')
                            return redirect('create_employee_user_super_admin')
                        else:
                            password = user_form.cleaned_data.get('password')
                            user_form = user_form.save(commit=False)
                            user_form.is_employee = True
                            user_form.created_by = user_name
                            user_form.password = AESCipher().encrypt(password)
                            user_form.save()
                            messages.success(request, 'Employee User Created Successfully!!')
                            return redirect('create_employee_user_super_admin')
                    context = {
                        'shop_users': shop_users,
                        'user_form': user_form,
                    }
                    return render(request, "admin/super_admin_user-form.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')


class CreateUserAdmin(View):

    @staticmethod
    def get(request):
        try:
            if request.session.get('admin'):
                user_name = request.session.get('admin')
                user_form = UserForm()
                shop_users = Users.objects.filter(created_by=user_name).order_by('employee_name')

                context = {
                    'user_form': user_form,
                    'shop_users': shop_users,
                }

                return render(request, "admin/super_admin_user-form.html", context)
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
        except Exception as e:
            print(e)
            return redirect('login')

    @staticmethod
    def post(request):
        try:
            if request.session.get('admin'):
                user_name = request.session.get('admin')
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
                    user_name = request.session.get('admin')
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
                    user_name = request.session.get('admin')

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
            else:
                messages.error(request, 'Session Expired!!')
                return redirect('login')
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
        except Exception as e:
            print(e)
            context = {
                'toast_type': 'error',
                'toast_message': 'User could not be Deleted!!',
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
