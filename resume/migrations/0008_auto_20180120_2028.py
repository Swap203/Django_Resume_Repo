# Generated by Django 2.0.1 on 2018-01-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20180119_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='birthDate',
            field=models.DateField(),
        ),
    ]
