from rest_framework import serializers
from react_app.models import Pokemon

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"
