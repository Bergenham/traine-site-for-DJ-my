from typing import Sequence
from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self,*args, **options):
        self.stdout.write('start')

        qs = Product.objects.values('pk', 'name')
        for obj in qs:
            print(obj)

        self.stdout.write('end')