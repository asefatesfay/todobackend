from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import TodoItem

def createItem(client):
    url=reverse('todoitem-list')
    data = {'title': 'Walk the dog'}
    return client.post(url, data, format='json')


class TestCreateTodoItem(APITestCase):
    """
     Ensure we can create a new todo item
    """
    def setUp(self):
        self.response = createItem(self.client)
    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    def test_received_location_header_hyperlink(self):
        self.assertRegexpMatches(self.response['Location'], '^http://.+/todos/[\d]+$')
    def test_item_is_created(self):
        self.assertEqual(TodoItem.objects.count(), 1)
    def test_item_have_correct_title(self):
        self.assertEqual(TodoItem.objects.get().title, 'Walk the dog')
