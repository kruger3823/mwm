# Generated by Django 4.0.6 on 2022-08-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MWMapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
