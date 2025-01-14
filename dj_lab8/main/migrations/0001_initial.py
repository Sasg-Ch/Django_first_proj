# Generated by Django 5.1.2 on 2024-10-11 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID клієнта')),
                ('customer_name', models.CharField(default='', max_length=255, verbose_name="Ім'я клієнта")),
                ('customer_address', models.CharField(default='', max_length=255, verbose_name='Адреса клієнта')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Телефон клієнта')),
                ('contact_person', models.CharField(default='', max_length=20, verbose_name='Контактна особа')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID предмета')),
                ('type', models.CharField(choices=[('Man', 'Чоловічий'), ('Girl', 'Жіночий'), ('Child', 'Дитячий')], default='', max_length=10, verbose_name='Тип')),
                ('name_item', models.CharField(default='', max_length=255, verbose_name='Назва одягу')),
                ('maker', models.CharField(default='', max_length=20, verbose_name='Виробник')),
                ('quantity', models.IntegerField(default=0, verbose_name='Кількість')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Ціна')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('storage_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID складу')),
                ('storage_address', models.CharField(default='', max_length=255, verbose_name='Адреса')),
                ('name_manager', models.CharField(default='', max_length=255, verbose_name='Завідувач складом')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sale_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID продажі')),
                ('sale_date', models.DateTimeField(auto_now_add=True, verbose_name='Час покупки')),
                ('buy_count', models.IntegerField(default=0, verbose_name='Кількість покупок')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Знижка')),
                ('code_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item', verbose_name='ID предмета')),
                ('customer_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer', verbose_name='ID клієнта')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='storage_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.storage', verbose_name='ID складу'),
        ),
    ]
