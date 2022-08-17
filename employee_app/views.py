from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from .models import *
from django.contrib import messages

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
            return redirect("index")

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


class MyView(View):

    @staticmethod
    def get(request):
        try:
            messages.success(request, 'Login Successful!!')
            return render(request, 'index.html')
        except Exception as e:
            print(e)
            return render(request, 'log-in.html', )

    @staticmethod
    def post(request):
        try:
            name = request.POST.get('name')
            print(name)
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
