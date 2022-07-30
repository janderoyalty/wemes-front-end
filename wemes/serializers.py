from rest_framework import serializers
from .models import *
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'phone_num', 'last_four', 'email', 'admin', 'is_active', 'transactions']

class TransactionSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'user_pk': 'user__pk',
    }

class ItemSerializer(NestedHyperlinkedModelSerializer):
    parent_lookup_kwargs = {
        'transition_pk': 'transition__pk',
        'user_pk': 'transition__user__pk',
    }

    class Meta:
        model = Item
        fields = ['id', 'drop_off', 'due_off', 'transaction', 'type', 'department', 'color']

    class Meta:
        model = Transaction
        fields = ['id', 'drop_off', 'admin', 'customer', 'items']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']

