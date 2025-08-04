from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from orders.models import Orders
from orders.serializers import OrderSerializer

class OrderCreateListView(generics.ListCreateAPIView):
    
    # queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        permission_classes = (IsAuthenticated, GlobalDefaultPermissions)
        queryset = Orders.objects.select_related('customer').all()
        
        customer_id = self.request.query_params.get('customer_id')

        if customer_id:
            try:
                queryset = queryset.filter(customer_id=int(customer_id))
            except (ValueError, TypeError):
                queryset = queryset.none()
            
        return queryset

class OrderRetriverUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
