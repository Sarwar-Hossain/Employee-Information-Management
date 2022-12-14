# Generated by Django 3.2.15 on 2022-08-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0009_alter_employee_employee_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographics',
            name='cell_phone',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='city_town',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='created_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='first_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='home_phone',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='last_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='social_security_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='state_zip_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='street_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='demographics',
            name='updated_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
