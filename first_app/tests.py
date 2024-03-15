from django.test import TestCase
from django.urls import reverse
from first_app.models import UserModel
from rest_framework.test import APIClient
from rest_framework import status


class UserCreatTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = UserModel.objects.create(email="test1@example.com", name="Test1", age=25)
        self.user2 = UserModel.objects.create(email="test2@example.com", name="Test2", age=30)


    def test_create_user(self):
        user_data = {
            "email": "kang@example.com",
            "name": "Test",
            "age": 21
        }
        url = reverse('users')
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(UserModel.objects.filter(email=user_data['email']).exists())

    def test_user_list(self):
        url = reverse('users')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_user_retrive(self):
        url = reverse('users', kwargs={'uuid': self.user1.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user1.email)

    def test_user_delete(self):
        url = reverse('users', kwargs={'uuid': self.user1.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)