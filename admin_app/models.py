from django.db import models


# Create your models here.

class Users(models.Model):
    objects = None

    employee_name = models.CharField(max_length=250, null=False)
    date_of_service = models.DateTimeField(null=False)
    medicaid_id = models.IntegerField(null=False)
    mobile_no = models.CharField(max_length=250, null=False)
    pa_name = models.CharField(max_length=250, null=False)
    employee_id = models.IntegerField(primary_key=True, null=False)
    is_active = models.BooleanField(null=True, default=True, blank=True)
    password = models.CharField(max_length=250, null=False)
    email = models.CharField(max_length=250, null=False, unique=True)
    is_admin = models.BooleanField(null=True, default=False, blank=True)
    is_employee = models.BooleanField(null=True, default=False, blank=True)
    is_super_admin = models.BooleanField(null=True, default=False, blank=True)
    nid_img = models.ImageField(upload_to="nid_images/", null=False, blank=False, default='nid_img/default.jpg')
    employee_img = models.ImageField(upload_to="employee_images/", null=False, blank=False,
                                     default='employee_img/default.jpg')

    created_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True)
    updated_at = models.DateTimeField(auto_now=False, null=True, blank=True)
