from rest_framework import serializers

from movies.models import Movie, Ratings


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(
        max_length=10, allow_blank=True, default=""
    )  # noqa
    rating = serializers.ChoiceField(choices=Ratings.choices, default=Ratings.G)  # noqa
    synopsis = serializers.CharField(allow_blank=True, default="")  # noqa
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
