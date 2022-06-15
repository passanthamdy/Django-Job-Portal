from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class DeveloperSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm', 'cv')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
            'cv': {'required': True},
        }

    def save(self, **kwargs):
        developer = User(
            username=self.validated_data.get('username'),
            email=self.validated_data.get('email'),
            cv=self.validated_data.get('cv'),
            user_type='DEVELOPER',
            # is_active=False
        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'detail': "passwords didn't match"}
            )
        else:
            developer.set_password(self.validated_data.get('password'))
            developer.save()
            return developer


class CompanySerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('company_name', 'address', 'email', 'password', 'password_confirm')
        extra_kwargs = {
            'company_name': {'required': True},
            'address': {'required': True},
            'email': {'required': True},
            'password': {'write_only': True, 'required': True},
        }

    def save(self, **kwargs):
        company = User(
            company_name=self.validated_data.get('company_name'),
            user_type='Company',
            # is_active=False
        )
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {'detail': "passwords didn't match"}
            )
        else:
            company.set_password(self.validated_data.get('password'))
            company.save()
            return company


