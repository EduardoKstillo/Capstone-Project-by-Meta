# myapp/tests.py

from django.test import TestCase
from restaurant.models import Menu

class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(title="Burger", price=5.99, inventory=10)

    def test_get_item(self):
        burger = Menu.objects.get(title="Burger")
        self.assertEqual(burger.get_item(), "Burger : 5.99")

    def test_str_representation(self):
        burger = Menu.objects.get(title="Burger")
        self.assertEqual(str(burger), "Burger")

    def test_inventory_default_value(self):
        burger = Menu.objects.get(title="Burger")
        self.assertEqual(burger.inventory, 10)  
