from django.test import TestCase

class TestNews(TestCase):
    def test_news_view(self):
        res = self.client.get('/news/')
        self.assertEqual(res.status_code, 200)