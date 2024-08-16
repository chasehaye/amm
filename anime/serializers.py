from rest_framework import serializers
from .models import Anime

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'titleEnglish']

    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance