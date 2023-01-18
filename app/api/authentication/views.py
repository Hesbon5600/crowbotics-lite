from dj_rest_auth.registration.views import RegisterView

from .serializers import RegisterSerializer


class CustomRegisterView(RegisterView):
    serializer_class = RegisterSerializer
