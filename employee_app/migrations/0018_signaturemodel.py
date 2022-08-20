# Generated by Django 3.2.15 on 2022-08-19 17:10

from django.db import migrations, models
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0017_employee_signature'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignatureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', jsignature.fields.JSignatureField()),
            ],
        ),
    ]
