from rest_framework import serializers
from account.models import Account

class AccountSerializer(serializers.ModelSerializer):

    accountname = serializers.ReadOnlyField(source='accountname.username')
    email = serializers.ReadOnlyField(source='accountname.email')
    isActive = serializers.ReadOnlyField(source='accountname.is_active')

    class Meta:
        model = Account
        fields = '__all__'