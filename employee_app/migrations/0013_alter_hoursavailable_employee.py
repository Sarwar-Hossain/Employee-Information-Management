# Generated by Django 3.2.15 on 2022-08-21 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0012_auto_20220821_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoursavailable',
            name='employee',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoursavailable', to='employee_app.employee'),
        ),
    ]
