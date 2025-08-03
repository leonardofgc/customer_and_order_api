from rest_framework import serializers
from customers.models import Customers
from orders.serializers import OrderSerializer

class CustomerSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customers
        fields = ['id', 'name', 'email', 'phone', 'created_at', 'orders']