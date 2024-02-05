# Generated by Django 5.0.1 on 2024-02-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='address',
            field=models.CharField(default=1, max_length=255, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='facebook',
            field=models.URLField(default=1, verbose_name='Facebook URL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='phone',
            field=models.CharField(default=1, max_length=255, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='twitter',
            field=models.URLField(default=1, verbose_name='Twitter URL'),
            preserve_default=False,
        ),
    ]