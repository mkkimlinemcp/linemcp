# Generated by Django 5.1.4 on 2025-01-19 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maincms', '0010_alter_rightholder_cr_create_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rightholder_cr',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='rightholder_cr',
            name='modify_date',
        ),
    ]