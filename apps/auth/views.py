from rest_framework_simplejwt.views import TokenObtainPairView

from apps.auth.serializers import TokenCustomSerializer


class TokenCustomView(TokenObtainPairView):
    serializer_class = TokenCustomSerializer
