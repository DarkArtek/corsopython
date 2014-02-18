from django.test import TestCase
import json

class BookTest(TestCase):
	def test_create(self):
		resp = self.client.post(
            '/book',
            '{"title": "Songlines" , "author": "Chetwin"}',
            HTTP_X_USERNAME='pippo',
            HTTP_X_PASSWORD='password',
            content_type='application/json')
		self.assertEqual(resp.status_code, 200)