from django.test import TestCase
from myapp.models import Menu, MenuCategory

class MenuTest(TestCase):
    def test_instance(self):        
        category = MenuCategory.objects.create(name='Desserts')

        item = Menu.objects.create(name='IceCream',price=80,category=category, description='description.')
        self.assertEqual(item.name, 'IceCream')
        self.assertEqual(item.price, 80)
        self.assertEqual(item.category_id, category)
        self.assertEqual(item.description, 'description.')