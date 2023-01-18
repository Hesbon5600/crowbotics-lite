from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import PasswordResetView

from . import serializers


class CustomRegisterView(RegisterView):
    """
    - Register a new user
    """

    serializer_class = serializers.RegisterSerializer


class CustomPasswordResetView(PasswordResetView):
    """
    - Reset password
    """

    serializer_class = serializers.CustomPasswordResetSerializer
