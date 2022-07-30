from rest_framework import serializers
from .models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'drop_off', 'due_off', 'customer_id', 'transaction_id', 'type', 'department', 'color']

class TransactionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Transaction
        fields = ['id', 'drop_off', 'admin', 'customer', 'items']


class UserSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(read_only=True, many=True)
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_num', 'last_four', 'email', 'admin', 'is_active', 'transactions']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

