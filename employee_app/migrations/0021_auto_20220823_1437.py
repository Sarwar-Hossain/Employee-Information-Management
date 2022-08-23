# Generated by Django 3.2.15 on 2022-08-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0020_auto_20220823_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transportation',
            name='is_bus_train_car',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='is_permission_for_criminal_background',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='is_personal_assistant_guide',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='is_valid_licenses',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='printed_name',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='routes',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
