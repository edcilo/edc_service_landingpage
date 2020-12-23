from rest_framework import serializers

from .models import Landing, Contact


class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = ['name', 'schema']


class ContactSerializer(serializers.ModelSerializer):
    message = serializers.CharField(min_length=4, max_length=2048)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
