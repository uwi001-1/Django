from rest_framework import serializers
from ..models import AccountsManagement
from django.core.cache import cache

class PasswordNumberSerializer(serializers.Serializer):
    email = serializers.EmailField()
    # type = serializers.ChoiceField(choices=[
    #     ('verification', 'Verification'),
    #     ('reset_password', 'Reset Password')
    # ])

def TokenValidate(token,email,key):
    # two line missing
    user = user.first()
    user_check_key = key + str(user.id)
    token_access = cache.get(user_check_key)
    if token_access == token:
        user.is_verified = True
        user.save()
        return True
    return False

class TokenValidationsSerializer(serializers.Serializer):
    otp = serializers.CharField()
    email = serializers.CharField()

    def validate_otp(self, value):
        # Perform token validation 
        email = self.initial_data.get('email') #Access email from initial data
        if not TokenValidate(value,email,"password_reset_otp_"):
            raise serializers.ValidationError("Invalid token")
        return value
    