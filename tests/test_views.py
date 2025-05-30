from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        MenuItem.objects.create(title="Burger", price=12.50, inventory=50)
        MenuItem.objects.create(title="Pizza", price=15.00, inventory=75)
        MenuItem.objects.create(title="Salad", price=8.75, inventory=30)

    def test_getall(self):
        menus = MenuItem.objects.all()
        serializer = MenuSerializer(menus, many=True)
        response = self.client.get(reverse('menu-items'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)