from django.test import TestCase
from rest_framework.test import APIClient
from myapp.models import Menu
from myapp.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = Menu.objects.create(title="Item 1", price=1.00, category=1, description='..')
        self.menu_item2 = Menu.objects.create(title="Item 2", price=1.00, category=1, description='..')

    def test_getall(self):
        response = self.client.get('/menu/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)