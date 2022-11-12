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


class CreateUserSuperAdmin(View):

    @staticmethod
    def get(request):
        try:
            if request.session.get('super_admin'):
                admin = None
                super_admin = request.session.get('super_admin')
                employee = None
                is_admin = False
                is_super_admin = False
                is_employee = False

                if super_admin:
                    user_role = Users.objects.get(employee_id=super_admin)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                        admin = user_role.employee_id
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                        super_admin = user_role.employee_id
                    else:
                        is_employee = user_role.is_employee
                        employee = user_role.employee_id

                user_form = UserForm()
                shop_users = Users.objects.all().order_by('employee_name')

                context = {
                    'super_admin': super_admin,
                    'user_form': user_form,
                    'shop_users': shop_users,
                }
                request.session['super_admin'] = super_admin
                request.session['admin'] = admin
                request.session['employee'] = employee
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
                admin = None
                super_admin = request.session.get('super_admin')
                employee = None
                created_by_id = None
                is_admin = False
                is_super_admin = False
                is_employee = False

                if super_admin:
                    user_role = Users.objects.get(employee_id=super_admin)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                        admin = user_role.employee_id
                        created_by_id = user_role.employee_id
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                        super_admin = user_role.employee_id
                        created_by_id = user_role.employee_id
                    else:
                        is_employee = user_role.is_employee
                        employee = user_role.employee_id

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
                            'super_admin': super_admin,
                        }

                        messages.success(request, 'User Selected!!')
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        return render(request, "admin/super_admin_user-form.html", context)
                    else:
                        user_form = UserForm(instance=user, initial={'password': password, 'user_role': 'employee'})
                        context = {
                            'shop_users': shop_users,
                            'user_form': user_form,
                            'single_user': user,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
                            'super_admin': super_admin,
                        }
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        messages.success(request, 'User Selected!!')
                        return render(request, "admin/super_admin_user-form.html", context)

                elif request.method == "POST" and request.POST.get('user_deactivate'):

                    user_deactivate_id = request.POST.get('user_deactivate')
                    Users.objects.filter(employee_id=user_deactivate_id).update(is_active=False, )
                    request.session['super_admin'] = super_admin
                    request.session['admin'] = admin
                    request.session['employee'] = employee
                    messages.success(request, 'User Deactivate Successfully!!')
                    return redirect('create_employee_user_super_admin')

                elif request.method == "POST" and request.POST.get('user_activate'):

                    user_activate_id = request.POST.get('user_activate')
                    Users.objects.filter(employee_id=user_activate_id).update(is_active=True, )
                    request.session['super_admin'] = super_admin
                    request.session['admin'] = admin
                    request.session['employee'] = employee
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
                            user.is_admin = False
                            user.updated_by = user_name
                            user.password = AESCipher().encrypt(password)
                            user.save()
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
                            messages.success(request, 'User Updated Successfully!!')
                            return redirect('create_employee_user_super_admin')
                        else:
                            password = user_form.cleaned_data.get('password')
                            user = user_form.save(commit=False)
                            user.updated_at = datetime.now()
                            user.is_employee = True
                            user.is_admin = True
                            user.updated_by = user_name
                            user.password = AESCipher().encrypt(password)
                            user.save()
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
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
                            user_form.created_by_id = created_by_id
                            user_form.password = AESCipher().encrypt(password)
                            user_form.save()
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
                            messages.success(request, 'Admin User Created Successfully!!')
                            return redirect('create_employee_user_super_admin')
                        else:
                            password = user_form.cleaned_data.get('password')
                            user_form = user_form.save(commit=False)
                            user_form.is_employee = True
                            user_form.is_admin = False
                            user_form.created_by_id = created_by_id
                            user_form.password = AESCipher().encrypt(password)
                            user_form.save()
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
                            messages.success(request, 'Employee User Created Successfully!!')
                            return redirect('create_employee_user_super_admin')
                    context = {
                        'shop_users': shop_users,
                        'user_form': user_form,
                    }
                    request.session['super_admin'] = super_admin
                    request.session['admin'] = admin
                    request.session['employee'] = employee
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
                admin = request.session.get('admin')
                super_admin = None
                employee = None
                created_by_id = None
                is_admin = False
                is_super_admin = False
                is_employee = False

                if admin:
                    user_role = Users.objects.get(employee_id=admin)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                        admin = user_role.employee_id
                        created_by_id = user_role.employee_id
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                        super_admin = user_role.employee_id
                        created_by_id = user_role.employee_id
                    else:
                        is_employee = user_role.is_employee
                        employee = user_role.employee_id

                user_form = UserForm()
                shop_users = Users.objects.filter(created_by_id=created_by_id).order_by('employee_name')

                context = {

                    'admin': admin,
                    'user_form': user_form,
                    'shop_users': shop_users,

                }

                request.session['super_admin'] = super_admin
                request.session['admin'] = admin
                request.session['employee'] = employee
                return render(request, "admin/admin_user_form.html", context)

            elif request.session.get('super_admin'):
                admin = None
                super_admin = request.session.get('super_admin')
                employee = None
                is_admin = False
                is_super_admin = False
                is_employee = False

                if super_admin:
                    user_role = Users.objects.get(employee_id=super_admin)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                        admin = user_role.employee_id
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                        super_admin = user_role.employee_id
                    else:
                        is_employee = user_role.is_employee
                        employee = user_role.employee_id

                user_form = UserForm()
                shop_users = Users.objects.all().order_by('employee_name')

                context = {
                    'super_admin': super_admin,
                    'user_form': user_form,
                    'shop_users': shop_users,
                }
                request.session['super_admin'] = super_admin
                request.session['admin'] = admin
                request.session['employee'] = employee
                return redirect('create_employee_user_super_admin')
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
                admin = request.session.get('admin')
                super_admin = None
                employee = None
                is_admin = False
                is_super_admin = False
                is_employee = False
                created_by_id = None

                if admin:
                    user_role = Users.objects.get(employee_id=admin)
                    if user_role.is_admin:
                        is_admin = user_role.is_admin
                        admin = user_role.employee_id
                        created_by_id = user_role.employee_id
                    elif user_role.is_super_admin:
                        is_super_admin = user_role.is_super_admin
                        super_admin = user_role.employee_id
                        created_by_id = user_role.employee_id
                    else:
                        is_employee = user_role.is_employee
                        employee = user_role.employee_id

                shop_users = Users.objects.filter(created_by_id=created_by_id).order_by('employee_name')
                employee_id = request.POST.get('button_select')
                if request.method == "POST" and request.POST.get('button_select'):
                    user = Users.objects.get(employee_id=employee_id)
                    decoded_pass = eval(user.password)
                    password = AESCipher().decrypt(decoded_pass)

                    if user.is_employee is True:
                        user_form = UserForm(instance=user, initial={'password': password, 'user_role': 'employee'})
                        context = {
                            'shop_users': shop_users,
                            'user_form': user_form,
                            'single_user': user,
                            'nid_img': user.nid_img,
                            'employee_img': user.employee_img,
                            'admin': admin,
                        }
                        messages.success(request, 'User Selected!!')
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        return render(request, "admin/admin_user_form.html", context)
                    else:
                        messages.error(request, 'User Role is Not Employee!!')
                        request.session['super_admin'] = super_admin
                        request.session['admin'] = admin
                        request.session['employee'] = employee
                        return redirect('create_employee_user_admin')

                elif request.method == "POST" and request.POST.get('user_deactivate'):

                    user_deactivate_id = request.POST.get('user_deactivate')
                    Users.objects.filter(employee_id=user_deactivate_id).update(is_active=False, )
                    messages.success(request, 'User Deactivate Successfully!!')
                    request.session['super_admin'] = super_admin
                    request.session['admin'] = admin
                    request.session['employee'] = employee
                    return redirect('create_employee_user_admin')

                elif request.method == "POST" and request.POST.get('user_activate'):

                    user_activate_id = request.POST.get('user_activate')
                    Users.objects.filter(employee_id=user_activate_id).update(is_active=True, )
                    messages.success(request, 'User Activate Successfully!!')
                    request.session['super_admin'] = super_admin
                    request.session['admin'] = admin
                    request.session['employee'] = employee
                    return redirect('create_employee_user_admin')

                elif request.method == "POST" and request.POST.get('button_update'):
                    user_name = request.session.get('admin')
                    update_user_id = request.POST.get('button_update')
                    user = Users.objects.get(employee_id=update_user_id)
                    user_form = UserForm(request.POST, request.FILES, instance=user)
                    if user_form.is_valid():
                        user_role = user_form.cleaned_data.get('user_role')
                        if user_role == 'admin':
                            user = Users.objects.get(employee_id=update_user_id)
                            decoded_pass = eval(user.password)
                            password = AESCipher().decrypt(decoded_pass)
                            user_form = UserForm(instance=user, initial={'password': password})
                            context = {
                                'shop_users': shop_users,
                                'user_form': user_form,
                                'single_user': user,
                                'admin': admin,
                            }
                            messages.error(request, 'You Are Not Permitted to Update User to Admin!!')
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
                            return render(request, "admin/admin_user_form.html", context)

                        else:
                            password = user_form.cleaned_data.get('password')
                            user_form = user_form.save(commit=False)
                            user_form.is_employee = True
                            user_form.is_admin = False
                            user_form.created_by_id = created_by_id
                            user_form.password = AESCipher().encrypt(password)
                            user_form.save()
                            messages.success(request, 'Employee User Updated Successfully!!')
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
                            return redirect('create_employee_user_admin')

                else:
                    user_form = UserForm(request.POST or None, request.FILES)
                    user_name = request.session.get('admin')

                    if request.method == "POST" and user_form.is_valid():
                        user_role = user_form.cleaned_data.get('user_role')
                        if user_role == 'admin':
                            messages.error(request, 'You Are Not Permitted to Create Admin User!!')
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
                            return redirect('create_employee_user_admin')
                        else:
                            password = user_form.cleaned_data.get('password')
                            user_form = user_form.save(commit=False)
                            user_form.is_employee = True
                            user_form.is_admin = False
                            user_form.created_by_id = created_by_id
                            user_form.password = AESCipher().encrypt(password)
                            user_form.save()
                            messages.success(request, 'Employee User Created Successfully!!')
                            request.session['super_admin'] = super_admin
                            request.session['admin'] = admin
                            request.session['employee'] = employee
                            return redirect('create_employee_user_admin')

                    context = {
                        'shop_users': shop_users,
                        'user_form': user_form,
                        'admin': admin,

                    }
                    request.session['super_admin'] = super_admin
                    request.session['admin'] = admin
                    request.session['employee'] = employee
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
