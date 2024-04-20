from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="username already taken."
            )
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="email already registered.",  # noqa
            )
        ],
    )
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False, allow_null=True)
    password = serializers.CharField(max_length=128, write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    class CustomJWTSerializer(TokenObtainPairSerializer):
        @classmethod
        def get_token(cls, user):
            token = super().get_token(user)
            token["is_superuser"] = user.is_superuser
            token["is_employee"] = user.is_employee

            return token

    def update(self, instace: User, validated_data: dict):
        for key, value in validated_data.items():
            if key == "password":
                instace.set_password(value)
            else:
                setattr(instace, key, value)

        instace.save()
        return instace
