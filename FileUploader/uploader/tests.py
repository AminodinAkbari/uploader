from rest_framework.test import APITestCase
from uploader.models import UploadedFile
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIRequestFactory
factory = APIRequestFactory()


# Create your tests here.
class BaseTest(APITestCase):
	def setUp(self):
		User.objects.create_user(username='TestUser' , password = '123456789')
		UploadedFile.objects.create(
			user = User.objects.get(id=1),
			type = 'text' ,
			size = '1000'
		)

		"""POSTING IS GENERIC VIEW NOT NEED TO TEST"""

	def test_get_infos(self):
		print('GET Method')
		response = self.client.get(reverse('get_method'))
		self.assertEqual(response.status_code , 200)

	def test_delete_api(self):
		print('DELETE Method')
		response = self.client.get(reverse('deleting' , kwargs={'pk':1}))
		print(response.status_code)