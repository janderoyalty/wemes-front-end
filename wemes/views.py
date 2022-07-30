from .models import *
from rest_framework import generics, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# USERS
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

# TRANSACTIONS
class TranList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

# USER
class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

# TRANS
class UserTransList(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

# USER -> TRANSACTIONS
class TransactionList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Transaction.objects.filter(customer_id=self.kwargs["pk"])
        return queryset
    serializer_class = TransactionSerializer

# TRANSACTIONS -> ITEMS
class TransItemsList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Item.objects.filter(transaction_id=self.kwargs["pk"])
        return queryset
    serializer_class = ItemSerializer

# class ItemList(generics.ListCreateAPIView):
#     def get_queryset(self):
#         queryset = Item.objects.filter(customer_id=self.kwargs["pk"], transaction_id=self.kwargs["pk"])
#         return queryset
#     serializer_class = ItemSerializer

class ItemsList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ItemSerializer
    permission_class = [permissions.IsAuthenticated]