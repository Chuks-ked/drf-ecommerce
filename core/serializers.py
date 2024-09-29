from djoser.serializers import UserCreateSerializer as UCS
from rest_framework import serializers



class UserCreateSerializer(UCS):
    # birth_date = serializers.DateField(read_only=True)

    class Meta(UCS.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
