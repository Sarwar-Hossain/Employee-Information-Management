# Generated by Django 3.2.15 on 2022-08-30 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_rename_member_name_users_employee_name'),
        ('employee_app', '0029_alter_demographics_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acknowledgementofreceipt',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acknowledgementreceipt', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='agreementwithcompany',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agreement', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='authorizationbackgroundcheck',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backgroundcheck', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='benefitportioncompensation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benefitportioncompensation', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='depositauthorization',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='depositauthorization', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='disclosuredrugtesting',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disclosuredrugtesting', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='drugtestguidelines',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drugtestguidelines', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='employeeacknowledgement',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employeeacknowledgement', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='informationattestation', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='employeewithholdingallowancecertificate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withholdingallowance', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='employeewithholdingcertificate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employeewithholdingcertificate', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='employerinformation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employerinformation', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='employerreviewverification',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employerreviewr', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='employmentfirstday',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employmentfirstday', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='hoursavailable',
            name='employee',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hoursavailable', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noticeacknowledgement', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='professionaltraining',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professionaltraining', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='reverificationrehires',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reverificationrehires', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='skillschecklist',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skillschecklist', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='translatorcertificate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transportation', to='admin_app.users'),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voluntaryidentification', to='admin_app.users'),
        ),
    ]
