from rest_framework import serializers
from todo.models import TodoItem

class TodoItemSerializers(serializers.HyperlinkedModelSerializer):
    url = serializers.ReadOnlyField()
    class Meta:
        model = TodoItem
        fields = ('url', 'title', 'completed', 'order')