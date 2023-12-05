from django.test import TestCase
from django.urls import reverse
from ..models import Menu
from ..serializers import MenuSerializer
import json

class MenuViewTest(TestCase):
    def setUp(self):
        menu1 = Menu.objects.create(title='Oranges', price=4.35, inventory=100)
        menu2 = Menu.objects.create(title='Moroccan Salad', price=5.00, inventory=9)

    def test_getall(self):
        url = reverse('menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        serialized_data = serializer.data

        expected_data = json.dumps(serialized_data)

        self.assertJSONEqual(response.content.decode('utf-8'), expected_data)
