# Generated by Django 5.1.4 on 2025-01-14 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincms', '0006_album_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test1', models.TextField()),
                ('test2', models.TextField()),
                ('test3', models.TextField()),
                ('test4', models.TextField()),
                ('test5', models.TextField()),
                ('test6', models.TextField()),
                ('test7', models.TextField()),
            ],
        ),
    ]