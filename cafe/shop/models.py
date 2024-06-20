from django.db import models

MAX_LENGTH = 255

class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    create_data = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    update_data = models.DateField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография блюда')
    is_exists = models.BooleanField(default=True, verbose_name='Добавить в меню или нет?')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-price']