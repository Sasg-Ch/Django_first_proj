from django.core.management.base import BaseCommand
from ...models import Storage,Customer,Item,Sale
from faker import Faker
import random

fake = Faker()


class Command(BaseCommand):
    help = 'Заполняет базу данных данными'

    def handle(self, *args, **kwargs):
        for _ in range(22):
            customer_code = random.randint(8, 14)
            code_item = random.randint(1, 17)
            sold_count = random.randint(1, 10)
            discount = round(random.uniform(0, 50), 2)
            item_instance = Item.objects.get(item_id=code_item)
            customer_instance = Customer.objects.get(customer_id=customer_code)

            Sale.objects.create(
                customer_code=customer_instance,
                code_item=item_instance,
                buy_count=sold_count,
                discount=discount
            )