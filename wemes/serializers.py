from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_num', 'last_four', 'email', 'admin', 'is_active']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'drop_off', 'admin', 'customer']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'drop_off', 'due_off', 'transaction', 'type', 'department', 'color']

