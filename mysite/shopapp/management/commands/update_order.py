from typing import Sequence

from django.core.management import BaseCommand
from shopapp.models import Order, Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start")
        order = Order.objects.first()
        if not order:
            self.stdout.write("Note Found")
            return

        products: Sequence[Product] = Product.objects.all()
        for i in products:
            order.products.add(i)
        order.save()
        self.stdout.write(f"Save connecting {order.products.all()} to {order}")