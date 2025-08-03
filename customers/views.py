from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermissions
from customers.models import Customers
from customers.serializers import CustomerSerializer
from customers.permissions import CustomerPermission

class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes  = (IsAuthenticated, GlobalDefaultPermissions)
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermissions,)
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
