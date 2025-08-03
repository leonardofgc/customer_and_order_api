from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerCreateListView.as_view(), name='customers-create-and-list'),
    path('customer/<int:pk>/', views.CustomerRetriveUpdateDestroyView.as_view(), name='customer-retrive-and-update-and-destroy'),
]