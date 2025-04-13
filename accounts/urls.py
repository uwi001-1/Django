from django.urls import path, include
from .viewsets.login import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('auth/login/', LoginView.as_view()),
    # path('auth/logout/', LogOutView.as_view(), name='logout'),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('token_verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('google_login/', views.GoogleLogin.as_view(), name='GoogleLogin'),
]