from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        midel = Movie
        fields = ('title', 'tagline')

