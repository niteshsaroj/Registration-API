from rest_framework import serializers
from .models import UserProfile
from rest_framework.validators import UniqueValidator

def no_space_validator(value):
    if ' ' in value:
        raise serializers.ValidationError("No spaces allowed.")
    return value

class UserProfileSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    username = serializers.CharField(
        validators=[
            no_space_validator,
            UniqueValidator(queryset=UserProfile.objects.all())
        ]
    )

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )

    age = serializers.IntegerField(min_value=13)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'age', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove non-model field
        return UserProfile.objects.create(**validated_data)
