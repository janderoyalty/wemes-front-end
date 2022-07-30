from .models import Item, User, Transaction
from rest_framework import viewsets, permissions, generics
from .serializers import UserSerializer, TransactionSerializer, ItemSerializer

# from django.http import JsonResponse
# from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def list(self, request,):
        queryset = User.objects.filter()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter()
        user = generics.get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer

    def list(self, request, user_pk=None):
        queryset = Transaction.objects.filter(user=user_pk)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None):
        queryset = Transaction.objects.filter(pk=pk, user=user_pk)
        transaction = generics.get_object_or_404(queryset, pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def list(self, request, user_pk=None, transition_pk=None):
        queryset = Item.objects.filter(transaction__user=user_pk, transaction=transition_pk)
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, user_pk=None, transition_pk=None):
        queryset = Item.objects.filter(pk=pk, transaction=transition_pk, transaction__user=user_pk)
        transition = generics.get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(transition)
        return Response(serializer.data)