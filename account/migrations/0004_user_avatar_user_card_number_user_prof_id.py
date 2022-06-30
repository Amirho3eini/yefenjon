# Generated by Django 4.0.5 on 2022-06-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=None, upload_to='avatars', verbose_name='آواتار'),
        ),
        migrations.AddField(
            model_name='user',
            name='card_number',
            field=models.IntegerField(default=0, verbose_name='شماره حساب'),
        ),
        migrations.AddField(
            model_name='user',
            name='prof_id',
            field=models.SlugField(default=None, max_length=200, verbose_name='آیدی'),
        ),
    ]
