from django.core.management import BaseCommand
from django.contrib.auth.models import User
from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Create Order")
        order = Order.objects.first()
        if not order:
            self.stdout.write("Note Found")
            return
        product = Product.objects.all()
        for i in product:
            order.products.add(i)
            self.stdout(f'add new product --- "{i}"')
        order.save()
