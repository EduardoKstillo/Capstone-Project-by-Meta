# myapp/tests.py

from django.test import TestCase
from .models import MenuItem

class MenuItemTestCase(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Burger", price=5.99, inventory=10)

    def test_get_item(self):
        burger = MenuItem.objects.get(title="Burger")
        self.assertEqual(burger.get_item(), "Burger : 5.99")

    def test_str_representation(self):
        burger = MenuItem.objects.get(title="Burger")
        self.assertEqual(str(burger), "Burger")

    def test_inventory_default_value(self):
        burger = MenuItem.objects.get(title="Burger")
        self.assertEqual(burger.inventory, 10)  # Suponiendo que el valor predeterminado del inventario es 10

    def test_price_type(self):
        burger = MenuItem.objects.get(title="Burger")
        self.assertIsInstance(burger.price, float)  # Suponiendo que el tipo de dato del precio es decimal
