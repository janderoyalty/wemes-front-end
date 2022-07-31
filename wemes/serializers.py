from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_num', 'last_four', 'email', 'admin', 'is_active', 'transactions']

class TransactionSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
        'user': 'user',
    }
    class Meta:
        model = Transaction
        fields = ['id', 'drop_off', 'admin', 'customer', 'items', "description"]

class ItemSerializer(serializers.ModelSerializer):
    parent_lookup_kwargs = {
    'item': 'item_h',
    'user': 'item_h__user',
    }
    class Meta:
        model = Item
        fields = ['id', 'drop_off', 'due_off', 'transaction', 'type', 'color', "is_shoe", "follow_up", "description"]

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

