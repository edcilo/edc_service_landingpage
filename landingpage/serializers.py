from rest_framework import serializers

from .models import Landing


class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = ['name', 'schema']
