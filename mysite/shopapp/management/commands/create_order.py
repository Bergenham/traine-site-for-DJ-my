from typing import Sequence
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django.db import transaction
from mysite.shopapp.models import Order, Product


class Command(BaseCommand):
    @transaction.atomic #если есть ошибка то не работает
    def handle(self,*args, **options):
        self.stdout.write('start')
        user = User.objects.get(usernaem='0')
        product: Sequence[Product] = Product.objects.all()
        order, status = Order.objects.get_ot_create(
            delivery_adres='dasdasd',
            promocod='p',
            user=user
        )
        for i in product:
            order.products.add(i)
        order.save()
        self.stdout.write('end')