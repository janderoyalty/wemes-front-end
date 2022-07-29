from .models import User, Transaction
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, TransactionSerializer

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("drop_off")
    serializer_class = TransactionSerializer
    permission_class = [permissions.IsAuthenticated]

    # @api_view(['PUT', 'DELETE'])
    # def user_details(request, pk):
    #     try:
    #         user = User.objects.get(pk=pk)
        
    #     except User.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'PUT' or request.method == 'DELETE':
    #         serializer = UserSerializer(user, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

