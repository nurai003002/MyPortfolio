# Generated by Django 5.0.1 on 2024-02-05 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_reviews_alter_partners_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image_news/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': '10) Новость',
                'verbose_name_plural': '10) Новости',
            },
        ),
    ]
