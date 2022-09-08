from django.db import models


# Create your models here.

class Users(models.Model):
    objects = None

    employee_name = models.CharField(max_length=250, null=False, blank=False, default=None)
    date_of_service = models.DateTimeField(null=False, blank=False, default=None)
    medicaid_id = models.IntegerField(null=False, blank=False, default=None)
    mobile_no = models.CharField(max_length=250, null=False, blank=False, default=None)
    pa_name = models.CharField(max_length=250, null=False, blank=False, default=None)
    employee_id = models.IntegerField(primary_key=True, null=False, blank=False, default=None)
    is_active = models.BooleanField(null=True, default=True, blank=True)
    password = models.CharField(max_length=250, null=False, blank=False, default=None)
    email = models.CharField(max_length=250, null=False, blank=False, unique=True, default=None)
    is_admin = models.BooleanField(null=True, default=False, blank=True)
    is_employee = models.BooleanField(null=True, default=False, blank=True)
    is_super_admin = models.BooleanField(null=True, default=False, blank=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
