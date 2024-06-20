from django.db import models


MAX_LENGTH = 255

class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название компании')
    agent_lastname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия представителя')
    agent_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя представителя')
    agent_surname = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Отчество представителя')
    phone = models.CharField(max_length=16, verbose_name='Телефон представителя')
    location = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес')
    is_exists = models.BooleanField(default=False, verbose_name='Логическое удаление')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        

class Supply(models.Model):
    date_supply = models.DateTimeField(auto_now_add=True, verbose_name='Дата поставки')
    supplier = models.OneToOneField(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик')
    
    product = models.ManyToManyField('Product', through='PosSupply', verbose_name='Товары')
    
    def __str__(self):
        return f'{self.date_supply} | {self.supplier.name}'
    
    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'
        

class Parametr(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Характеристика')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'
    

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Описание')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        

class Tag(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    description = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Описание')
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        

class Order(models.Model):
    PICKUP = 'PK'
    COURIER = 'CR'
    DELIVERY_CHOICES = [
        (PICKUP, 'Самовывоз'),
        (COURIER, 'Курьер'),
    ]
    
    count = models.PositiveIntegerField(verbose_name='Номер заказа')
    customer_lastname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия заказчика')
    customer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя заказчика')
    customer_surname = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Отчество заказчика')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    location = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Адрес доставки')
    delivery = models.CharField(max_length=2, choices=DELIVERY_CHOICES, verbose_name='Способ доставки')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    completion_data = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения')
    
    product = models.ManyToManyField('Product', through='PosOrder', verbose_name='Товар')
    
    def __str__(self):
        return f'{self.count} | {self.location}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        

class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, unique=True, verbose_name='Название')
    desctipriont = models.CharField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    create_data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_data = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='images/%Y/%m/%d', default='images/no_photo.png', verbose_name='Картинка')
    is_exists = models.BooleanField(default=False, verbose_name='Логическое удаление')
    
    parament = models.ManyToManyField(Parametr, through='PosParametr', verbose_name='Характеристика')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категории')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', '-price']


class PosParametr(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    parametr = models.ForeignKey(Parametr, on_delete=models.PROTECT, verbose_name='Характеристика')
    value = models.CharField(max_length=MAX_LENGTH, verbose_name='Значение')
    
    def __str__(self):
        return f'{self.product.name} | {self.value}'
    
    class Meta:
        verbose_name = 'Характеристика товара'
        verbose_name_plural = 'Характеристики товаров'
        

class PosOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    count = models.PositiveIntegerField(verbose_name='Количество')
    discount = models.PositiveIntegerField(verbose_name='Скидка')
    
    def __str__(self):
        return f'{self.order.count} | {self.product.name} ({self.count})'
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
        

class PosSupply(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    supply = models.ForeignKey(Supply, on_delete=models.PROTECT, verbose_name='Поставка')
    count = models.PositiveIntegerField(verbose_name='Кол-во товара')
    
    def __str__(self):
        return f'{self.supply.date_supply} | {self.product.name} ({self.count})'
    
    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставок'
    
        
class WareHouse(models.Model):
    ALL = 'AL'
    AIRPLANE = 'AR'
    TRAIN = 'TR'
    TRACK = 'TK'
    TYPE_POST = [
        (ALL, 'Любой вид отправки'),
        (AIRPLANE, 'Отправка самолётом'),
        (TRAIN, 'Отправка поездом'),
        (TRACK, 'Отправка грузовиком')
    ]
    owner_lastname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия владельца')
    owner_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя владельца')
    owner_surname = models.CharField(max_length=MAX_LENGTH, blank=True, null=True, verbose_name='Отчество владельца')
    location = models.CharField(max_length=MAX_LENGTH, verbose_name='Расположение')
    type_post = models.CharField(max_length=2, default=ALL, choices=TYPE_POST, verbose_name='Вид отправки')
    opacity = models.PositiveIntegerField(default = 10000, verbose_name='Вместимость')
    
    def __str__(self):
        return f'{self.location} ( {self.opacity} ячеек )'
    
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        
        
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    warehouse = models.ForeignKey(WareHouse, on_delete=models.CASCADE, verbose_name='Склад')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default = 0)
    single_position = models.FloatField(verbose_name='Вес одной позиции')
    
    def __str__(self):
        return f'{self.product.name} хранится в {self.product.pk} складе ({self.quantity})'
    
    class Meta:
        verbose_name = 'Хранение позиции'
        verbose_name_plural = 'Хранение позиций'
    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    user_name = models.CharField(max_length=MAX_LENGTH, default='anonim', verbose_name='NickName')
    rating = models.PositiveIntegerField(verbose_name='Оценка')
    commit = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    photo = models.ImageField(upload_to='images/review/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография')
    
    def __str__(self):
        return f'{self.user_name} | {self.product.name} - {self.rating}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'