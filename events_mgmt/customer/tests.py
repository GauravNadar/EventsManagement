from django.test import TestCase
from django.urls import reverse

class HomeViewTestCase(TestCase):

    def test_home_view_status(self):
        url = reverse("index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
