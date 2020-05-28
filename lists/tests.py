from django.test import TestCase


class HomePageTest(TestCase):

    def test_smoke_test(self):
        response = self.client.get('/')
        self.assertTrue(response.content.decode().startswith('<html>'))
        self.assertIn(
            '<title>To-Do lists</title>',
            response.content.decode()
        )
        self.assertTrue(response.content.decode().endswith('</html>'))