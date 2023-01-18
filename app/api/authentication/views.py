from dj_rest_auth.registration.views import RegisterView

from .serializers import RegisterSerializer


class CustomRegisterView(RegisterView):
    """
    - Register a new user
    """

    serializer_class = RegisterSerializer
