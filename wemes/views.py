from datetime import datetime, time, timedelta

from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from .models import Item, Transaction, User
from .serializers import *

# class NestedUserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.filter()

#     def list(self, request):
#         queryset = User.objects.filter()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, **kwargs):
#         queryset = User.objects.filter()
#         user = get_object_or_404(queryset, pk=kwargs['pk'])
#         serializer = UserSerializer(user)
#         return Response(serializer.data)


# class NestedTransactionViewSet(viewsets.ModelViewSet):
#     serializer_class = TransactionSerializer
#     queryset = Transaction.objects.filter()

#     def list(self, request, **kwargs):
#         queryset = Transaction.objects.filter(customer=kwargs['customer_pk'])
#         serializer = TransactionSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, **kwargs):
#         queryset = Transaction.objects.filter(pk=kwargs['pk'], customer=kwargs['customer_pk'])
#         transaction = get_object_or_404(queryset, pk=kwargs['pk'])
#         serializer = TransactionSerializer(transaction)
#         return Response(serializer.data)

# class NestedItemViewSet(viewsets.ModelViewSet):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.filter()

#     def list(self, request, **kwargs):
#         queryset = Item.objects.filter(transaction__customer=kwargs['customer_pk'], transaction=kwargs['transactions_pk'])
#         serializer = ItemSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, **kwargs):
#         print(request, kwargs)
#         queryset = Item.objects.filter(pk=kwargs['pk'], transaction=kwargs['transactions_pk'], transaction__customer=kwargs['customer_pk'])
#         item = get_object_or_404(queryset, pk=kwargs['pk'])
#         serializer = ItemSerializer(item)
#         return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_class = [permissions.IsAuthenticated]

class TransactionDateViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.filter()
    serializer_class = TransactionSerializer
    permission_class = [permissions.IsAuthenticated]

    def current(self, request, **kwargs):
        today = datetime.now().date()
        print(today)
        queryset = Transaction.objects.filter(pk=kwargs['pk'], transaction=kwargs['transactions_pk'], transaction__customer=kwargs['customer_pk'])
        item = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = TransactionSerializer(item)
        return Response(serializer.data)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_class = [permissions.IsAuthenticated]


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_class = [permissions.IsAuthenticated]


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_class = [permissions.IsAuthenticated]

