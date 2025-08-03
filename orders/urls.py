from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderCreateListView.as_view(), name='orders'),
    path('order/<int:pk>/', views.OrderRetriverUpdateDelete.as_view(), name='orders-detail-update-delete'),
]