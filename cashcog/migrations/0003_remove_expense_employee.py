# Generated by Django 3.0 on 2020-01-01 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashcog', '0002_auto_20200101_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='employee',
        ),
    ]
