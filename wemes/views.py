from .models import Item, User, Transaction
from rest_framework import viewsets
from .serializers import UserSerializer, TransactionSerializer, ItemSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter()

    def list(self, request):
        queryset = User.objects.filter()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        queryset = User.objects.filter()
        user = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = UserSerializer(user)
        return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.filter()

    def list(self, request, **kwargs):
        queryset = Transaction.objects.filter(customer=kwargs['customer_pk'])
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        queryset = Transaction.objects.filter(pk=kwargs['pk'], customer=kwargs['customer_pk'])
        transaction = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.filter()

    def list(self, request, **kwargs):
        queryset = Item.objects.filter(transaction__customer=kwargs['customer_pk'], transaction=kwargs['transactions_pk'])
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        queryset = Item.objects.filter(pk=kwargs['pk'], transaction=kwargs['transactions_pk'], transaction__customer=kwargs['customer_pk'])
        item = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = ItemSerializer(item)
        return Response(serializer.data)