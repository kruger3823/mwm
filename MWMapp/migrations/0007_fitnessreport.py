# Generated by Django 4.0.5 on 2022-08-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MWMapp', '0006_remove_insurance_scheme_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='fitnessreport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
