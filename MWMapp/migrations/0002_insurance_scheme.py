# Generated by Django 4.0.5 on 2022-08-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MWMapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='insurance_scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('add_scheme', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]