# Generated by Django 5.0.6 on 2024-06-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('create_data', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_data', models.DateField(auto_now=True, verbose_name='Дата изменения')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d', verbose_name='Фотография блюда')),
                ('is_exists', models.BooleanField(default=True, verbose_name='Добавить в меню или нет?')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name', '-price'],
            },
        ),
    ]
