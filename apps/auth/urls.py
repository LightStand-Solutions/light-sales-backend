from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.auth.views import TokenCustomView

urlpatterns = [
    path('login/', TokenCustomView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]
