# Generated by Django 4.2 on 2024-01-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgapp', '0023_album_auto_left_right'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='auto_wide_image',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='albumimage',
            name='wide',
            field=models.BooleanField(default=False),
        ),
    ]