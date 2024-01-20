from django.test import TestCase

class TestNews(TestCase):
    def test_history_view(self):
        res = self.client.get('/history/')
        self.assertEqual(res.status_code, 200)