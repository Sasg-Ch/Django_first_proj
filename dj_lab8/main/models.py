from django.db import models

# Create your models here.
class Storage(models.Model):
    storage_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID складу')
    storage_address = models.CharField('Адреса',max_length=255,default='')
    name_manager = models.CharField('Завідувач складом',max_length=255,default='')
    phone = models.CharField('Телефон',max_length=20, default='')

class Customer(models.Model):
    customer_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID клієнта')
    customer_name = models.CharField('Ім\'я клієнта',max_length=255,default='')
    customer_address = models.CharField('Адреса клієнта',max_length=255,default='')
    phone = models.CharField('Телефон клієнта',max_length=20, default='')
    contact_person = models.CharField('Контактна особа',max_length=20, default='')

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('Man', 'Чоловічий'),
        ('Girl', 'Жіночий'),
        ('Child', 'Дитячий'),
    ]
    item_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID предмета')
    type = models.CharField('Тип',choices=CATEGORY_CHOICES,max_length=10,default='')
    name_item = models.CharField('Назва одягу',max_length=255,default='')
    maker = models.CharField('Виробник',max_length=20, default='')
    storage_id = models.ForeignKey('Storage', on_delete=models.CASCADE, verbose_name='ID складу')
    quantity = models.IntegerField('Кількість', default=0)
    price = models.DecimalField('Ціна',decimal_places=2,max_digits=10,default=0.00)

class Sale(models.Model):
    sale_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID продажі')
    sale_date = models.DateTimeField('Час покупки', auto_now_add=True)
    customer_code = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='ID клієнта')
    code_item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name='ID предмета')
    buy_count = models.IntegerField('Кількість покупок', default=0)
    discount = models.DecimalField("Знижка",decimal_places=2,max_digits=10)

