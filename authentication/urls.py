from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('autenthication/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('autenthication/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('autenthication/token/verify/', TokenVerifyView.as_view(), name='token-verify')
]