# Generated by Django 3.2.15 on 2022-08-19 17:11

from django.db import migrations
import jsignature.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0018_signaturemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signaturemodel',
            name='signature',
            field=jsignature.fields.JSignatureField(max_length=1000),
        ),
    ]
