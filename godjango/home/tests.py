from django.utils import unittest
from django.test.client import Client

class UrlTestClass(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_200_on_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    #def test_200_on_video_page(self):
    #    response = self.client.get('/1-hello-world/')
    #    self.assertEqual(response.status_code, 200)

    def test_200_on_feedback_page(self):
        response = self.client.get('/feedback/')
        self.assertEqual(response.status_code, 200)

    def test_200_on_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
