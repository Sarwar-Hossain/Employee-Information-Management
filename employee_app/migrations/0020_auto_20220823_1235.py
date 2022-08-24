# Generated by Django 3.2.15 on 2022-08-23 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0019_alter_skillschecklist_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acknowledgementofreceipt',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acknowledgementreceipt', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='agreementwithcompany',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agreement', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='authorizationbackgroundcheck',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='backgroundcheck', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='benefitportioncompensation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benefitportioncompensation', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='depositauthorization',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='depositauthorization', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='disclosuredrugtesting',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disclosuredrugtesting', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='drugtestguidelines',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='drugtestguidelines', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='employeeacknowledgement',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employeeacknowledgement', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='informationattestation', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='employeewithholdingallowancecertificate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='withholdingallowance', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='employeewithholdingcertificate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employeewithholdingcertificate', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='employerinformation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employerinformation', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='employerreviewverification',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employerreviewr', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='employmentfirstday',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employmentfirstday', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noticeacknowledgement', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='reverificationrehires',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reverificationrehires', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='translatorcertificate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translator', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='transportation',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transportation', to='employee_app.employee'),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voluntaryidentification', to='employee_app.employee'),
        ),
    ]