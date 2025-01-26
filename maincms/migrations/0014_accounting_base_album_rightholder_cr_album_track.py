# Generated by Django 5.1.4 on 2025-01-22 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maincms', '0013_create_artist_profile_bugs_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting_base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album_code', models.IntegerField()),
                ('rightholder_code', models.IntegerField()),
                ('company_fees', models.FloatField()),
                ('User_Fees', models.FloatField()),
                ('Settlement_Status', models.BooleanField(blank=True)),
                ('Settlement_user', models.JSONField(default=list)),
                ('Settlement_rate', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_code', models.TextField()),
                ('album_title', models.TextField()),
                ('album_title_en', models.TextField(blank=True)),
                ('album_artist', models.TextField()),
                ('album_genre', models.TextField()),
                ('album_Categ', models.TextField()),
                ('album_country', models.TextField(blank=True)),
                ('startdate', models.TextField()),
                ('opendate', models.TextField()),
                ('service_time', models.TextField()),
                ('album_copyright', models.TextField()),
                ('album_publish', models.TextField()),
                ('service_area', models.TextField()),
                ('excluded', models.TextField(blank=True)),
                ('service_lang', models.TextField()),
                ('UPC_code', models.TextField(blank=True)),
                ('UCI_code', models.TextField(blank=True)),
                ('YT_service', models.TextField()),
                ('status', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='rightholder_cr',
            name='album',
            field=models.JSONField(default=list),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disk_no', models.IntegerField()),
                ('track_no', models.IntegerField()),
                ('track_code', models.TextField()),
                ('song_title', models.TextField()),
                ('song_artist', models.TextField()),
                ('track_genre', models.TextField()),
                ('track_lang', models.TextField()),
                ('title_song', models.TextField(blank=True)),
                ('adult', models.TextField(blank=True)),
                ('tr_opendate', models.TextField()),
                ('track_length', models.TextField()),
                ('lyricist', models.TextField(blank=True)),
                ('composer', models.TextField(blank=True)),
                ('arranger', models.TextField(blank=True)),
                ('with_artist', models.TextField(blank=True)),
                ('featured', models.TextField(blank=True)),
                ('UCI', models.TextField(blank=True)),
                ('ISRC', models.TextField(blank=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tracks', to='maincms.album')),
            ],
        ),
    ]