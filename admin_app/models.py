from django.db import models


# Create your models here.

class Users(models.Model):
    objects = None

    employee_name = models.CharField(max_length=250, null=True, blank=True)
    date_of_service = models.DateTimeField(null=True, blank=True)
    medicaid_id = models.IntegerField(null=True, blank=True)
    mobile_no = models.CharField(max_length=250, null=True)
    pa_name = models.CharField(max_length=250, null=True, blank=True, default=None)
    employee_id = models.IntegerField(primary_key=True, null=False, blank=True, default=None)
    is_active = models.BooleanField(null=True, default=True, blank=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    is_admin = models.BooleanField(null=True, default=False, blank=True)
    is_employee = models.BooleanField(null=True, default=True, blank=True)

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
