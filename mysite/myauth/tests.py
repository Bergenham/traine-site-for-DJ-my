import json
from django.test import TestCase
from django.urls import reverse

class GetCookieViewTestCase(TestCase):
    def test_get_cookie_view(self):
        response = self.client.get(reverse("myauth:get-cookie"))
        self.assertContains(response, 'Cookie value:')

class JsonFooTestCase(TestCase):
    def test_main(self):
        respounse = self.client.get(reverse('myauth:json'))
        self.assertEqual(respounse.status_code, 200)
        self.assertEqual(respounse.headers['content-type'], 'application/json',)
        was_be = {"foo": "bar", "spam": "ew"}
        self.assertJSONEqual(respounse.content, was_be)