from django.conf import settings
from string import ascii_letters
from random import choice
from django.urls import reverse
from django.test import TestCase
from .models import Product, User
from .utils import sumN


class SumNTest_Case(TestCase):
    def test_main(self):
        res = sumN(2, 1)
        self.assertEqual(res, 3)

class CreateProductViewTestCase(TestCase):
    def setUp(self):
        self.product_name = ''.join(choice(ascii_letters))
        Product.objects.filter(name=self.product_name).delete()

    def test_create(self):
        response = self.client.post(
            reverse('shopapp:product_input'),
            {
                'name': self.product_name
                , 'prise': '32'
                , 'description': 'feqdwqew'
                , 'discount': '2',
            }
        )
        self.assertRedirects(response, reverse("shopapp:product_list"))
        self.assertTrue(Product.objects.filter(name=self.product_name).exists())

class DetailsProductViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name="BANEN")

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    def test_detail(self):
        response = self.client.get(
            reverse('shopapp:product_details',
            kwargs={'pk': self.product.pk}
                    )
        )
        self.assertEqual(response.status_code, 200)

    def test_detail_context(self):
        response = self.client.get(
            reverse('shopapp:product_details',
            kwargs={'pk': self.product.pk}
                    )
        )
        self.assertContains(response, self.product.name)

class ProductListViewTestCase(TestCase):
    fixtures = [
        'product-fixture.json',
    ]

    def test_products(self):
        response = self.client.get(reverse("shopapp:product_list"))
        self.assertQuerysetEqual(
            qs=Product.objects.filter(arvay=False).all(),
            values=(p.pk for p in response.context["products"]),
            transform=lambda p: p.pk,
        )

class OrderListViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.dt = dict(username='Pe', password='23d')
        cls.user = User.objects.create_user(username='Pe', password='23d')

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_main(self):
        response = self.client.get(reverse('shopapp:order_list'))
        self.assertContains(response, 'Order')

    def test_orders_view_na(self):
        self.client.logout()
        response = self.client.get(reverse("shopapp:order_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)
