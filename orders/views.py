from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from orders.models import Orders
from orders.serializers import OrderSerializer

class OrderCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class OrderRetriverUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
