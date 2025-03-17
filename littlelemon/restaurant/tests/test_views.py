from django.test import TestCase
from restaurant.models import Menu
from django.core.serializers import serialize
from restaurant.serializers import MenuSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token #Import the Token model.
from django.contrib.auth.models import User
import json

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Pasta", price=100, inventory=30)
        Menu.objects.create(title="Salad", price=60, inventory=20)
        
        # * create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # * create a token
        self.token = Token.objects.create(user=self.user) #Create a token for the test user.
        
    def test_getall(self):
        
        url = reverse('menu')
        client = APIClient()
        # ! add if using session authentication
        client.force_login(self.user)
        # ! add if using token authentication
        #* client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = client.get(url)
        
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        
        self.assertEqual(response.data, serializer.data)