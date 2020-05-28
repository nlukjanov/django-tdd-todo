from django.test import TestCase


class HomePageTest(TestCase):

    def test_smoke_test(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home`.html')
