from django.core.management.base import BaseCommand
from cachingDemo.models import Products
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the Product table with 1000 products'

    def handle(self, *args, **kwargs):
        for i in range(1000):
            name = f'Product {i+1}'
            description = f'Description for Product {i+1}'
            price = random.uniform(10, 1000)  # Generate random price between 10 and 1000
            Products.objects.create(name=name, description=description, price=price)

        self.stdout.write(self.style.SUCCESS('Successfully populated the Product table with 1000 products.'))
