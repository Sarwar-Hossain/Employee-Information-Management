# Generated by Django 3.2.15 on 2022-08-23 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0015_auto_20220823_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionaltraining',
            name='entrance_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
