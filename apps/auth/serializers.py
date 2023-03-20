from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenCustomSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        data['id'] = self.user.id
        data['username'] = self.user.username
        data['client'] = self.user.client or None
        data['isSuperUser'] = self.user.is_superuser

        return data
