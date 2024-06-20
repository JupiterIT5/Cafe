# Generated by Django 5.0.6 on 2024-06-20 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_rename_full_characteristic_fullcharacteristic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_lastname', models.CharField(max_length=255, verbose_name='Фамилия владельца')),
                ('owner_name', models.CharField(max_length=255, verbose_name='Имя владельца')),
                ('owner_surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество владельца')),
                ('location', models.CharField(max_length=255, verbose_name='Расположение')),
                ('type_post', models.CharField(choices=[('AL', 'Любой вид отправки'), ('AR', 'Отправка самолётом'), ('TR', 'Отправка поездом'), ('TK', 'Отправка грузовиком')], default='AL', max_length=2, verbose_name='Вид отправки')),
                ('opacity', models.PositiveIntegerField(default=10000, verbose_name='Вместимость')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склады',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='lastname_customer',
            field=models.CharField(max_length=255, verbose_name='Фамилия покупателя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name_customer',
            field=models.CharField(max_length=255, verbose_name='Имя покупателя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='surname_customer',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Очество покупателя'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='lastname_provider',
            field=models.CharField(max_length=255, verbose_name='Фамилия представителя'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name_provider',
            field=models.CharField(max_length=255, verbose_name='Имя представителя'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='surname_provider',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Очество представителя'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='anonim', max_length=255, verbose_name='NickName')),
                ('rating', models.PositiveIntegerField(verbose_name='Оценка')),
                ('commit', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/review/%Y/%m/%d', verbose_name='Фотография')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('single_position', models.FloatField(verbose_name='Вес одной позиции')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.product', verbose_name='Товар')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.warehouse', verbose_name='Склад')),
            ],
            options={
                'verbose_name': 'Хранение позиции',
                'verbose_name_plural': 'Хранение позиций',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='warehouse',
            field=models.ManyToManyField(through='about.Inventory', to='about.warehouse', verbose_name='Склад'),
        ),
    ]
