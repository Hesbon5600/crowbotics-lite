from dj_rest_auth.serializers import PasswordResetSerializer
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    def save(self, request):
        """
        Override the save method to create a new user
        """
        user = User.objects.create_user(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
            password=self.validated_data["password"],
        )

        return user

    class Meta:
        model = User
        fields = ("username", "email", "password")


class CustomPasswordResetSerializer(PasswordResetSerializer):
    """
    - Override the default dj_rest_auth PasswordResetSerializer
      to customize token_generator
    """

    def save(self):

        request = self.context.get("request")
        # Set some values to trigger the send_email method.
        opts = {
            "use_https": request.is_secure(),
            "from_email": settings.DEFAULT_FROM_EMAIL,
            "request": request,
            "token_generator": PasswordResetTokenGenerator,
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
