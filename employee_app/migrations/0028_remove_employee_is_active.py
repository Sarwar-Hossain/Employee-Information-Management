# Generated by Django 3.2.15 on 2022-08-28 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0027_auto_20220828_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
    ]