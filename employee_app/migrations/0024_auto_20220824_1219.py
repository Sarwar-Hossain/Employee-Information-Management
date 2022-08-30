# Generated by Django 3.2.15 on 2022-08-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0023_auto_20220824_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositauthorization',
            name='is_checking',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='depositauthorization',
            name='is_savings',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employeeacknowledgement',
            name='is_notice_given',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='admission_no',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='alien_reg_no',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='apt_no',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='authorize_to_work',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='city_town',
            field=models.CharField(blank=True, default=None, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='country_of_issuance',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='employee_tp_no',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='foreign_passport_no',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='is_citizen_us',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='is_lawful_resident',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='is_non_citizen_us',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='middle_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='or_code',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='other_name',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='social_security_no',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinformationattestation',
            name='zip_code',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='is_at_hiring',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='is_before_change',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='is_bi_weekly',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='is_none',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='is_notice_in_english',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='noticeacknowledgement',
            name='is_weekly',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='translatorcertificate',
            name='is_preparer_assisted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='translatorcertificate',
            name='is_use_translator',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_american_indian_or_alaskan',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_armed_forces',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_asian',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_black_or_african_American',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_disabled_veteran',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_disclose_disability',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_disclose_info',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_disclose_military_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_disclose_sex',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_female',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_have_disability',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_hispanic_or_latino',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_male',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_middle_or_north_east',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_no_disability',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_no_military_status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_other_pacific_island',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_other_protected_veteran',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='voluntaryidentification',
            name='is_two_or_more_races',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
