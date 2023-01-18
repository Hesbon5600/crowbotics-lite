from rest_framework import generics, permissions

from . import models, serializers


class ApplicationCreateListView(generics.ListCreateAPIView):
    """
    - Create a new application
    - List all applications
    """

    serializer_class = serializers.ApplicationSerializer
    queryset = models.Application.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def filter_queryset(self, queryset):
        """
        Filter the queryset to only include applications for the current user
        """
        return queryset.filter(user=self.request.user)


class ApplicationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    - Retrieve an application
    - Update an application
    - Destroy an application
    """

    serializer_class = serializers.ApplicationSerializer
    queryset = models.Application.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        """
        Use different serializer for update
        """
        if self.request.method in ["PUT", "PATCH"]:
            return serializers.ApplicationUpdateSerializer

        return self.serializer_class

    def filter_queryset(self, queryset):
        """
        Filter the queryset to only include applications for the current user
        """
        return queryset.filter(user=self.request.user)


class PlanRetrieveView(generics.RetrieveAPIView):
    """
    - Retrieve a plan
    """

    serializer_class = serializers.PlanSerializer
    queryset = models.Plan.objects.all()
    permission_classes = (permissions.AllowAny,)


class PlanListView(generics.ListAPIView):
    """
    - List all plans
    """

    serializer_class = serializers.PlanSerializer
    queryset = models.Plan.objects.all()
    permission_classes = (permissions.AllowAny,)


class SubscriptionCreateListView(generics.ListCreateAPIView):
    """
    - Create a new subscription
    - List all subscriptions
    """

    serializer_class = serializers.SubscriptionSerializer
    queryset = models.Subscription.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def filter_queryset(self, queryset):
        """
        Filter the queryset to only include active subscriptions for the current user
        """
        return queryset.filter(application__user=self.request.user, active=True)


class SubscriptionRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    - Retrieve a subscription
    - Update a subscription
    """

    serializer_class = serializers.SubscriptionSerializer
    queryset = models.Subscription.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        """
        Use different serializer for update
        """
        if self.request.method in ["PUT", "PATCH"]:
            return serializers.SubscriptionUpdateSerializer

        return self.serializer_class

    def filter_queryset(self, queryset):
        """
        Filter the queryset to only include active subscriptions for the current user
        """
        return queryset.filter(user=self.request.user, active=True)
