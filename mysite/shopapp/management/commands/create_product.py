from collections.abc import Sequence
from django.core.management import BaseCommand
from shopapp.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Started to created command...")
        name = [
            'Laptop',
            'Desktop',
            'Smartphone'
        ]
        for i in name:
            product, status = Product.objects.get_or_create(name=i)
            self.stdout.write(f"Add Product -> {product}; Status -> {status}")
        self.stdout.write(self.style.SUCCESS('End of command'))