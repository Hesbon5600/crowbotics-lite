from rest_framework import serializers

from ..helpers.serialization_errors import error_dict
from . import models


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate_name(self, value):
        """
        Validate that the application name is unique for the user
        Args:
            value (str): The application name
        Returns:
            str: The application name
        Raises:
            serializers.ValidationError: If the application name already exists
        """
        if models.Application.objects.filter(
            name=value, user=self.context["request"].user
        ).exists():
            raise serializers.ValidationError(
                error_dict["already_exists"].format("Application name")
            )

        return value

    def validate_domain_name(self, value):
        """
        Validate that the domain name is unique for the user
        Args:
            value (str): The domain name
        Returns:
            str: The domain name
        Raises:
            serializers.ValidationError: If the domain name already exists
        """
        if models.Application.objects.filter(
            domain_name=value, user=self.context["request"].user
        ).exists():
            raise serializers.ValidationError(
                error_dict["already_exists"].format("Domain name")
            )

        return value

    class Meta:
        model = models.Application
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        """
        Validate that the application name is unique for the user
        Args:
            value (str): The application name
        Returns:
            str: The application name
        Raises:
            serializers.ValidationError: If the application name already exists
        """
        if (
            models.Application.objects.filter(
                name=value, user=self.context["request"].user
            )
            .exclude(id=self.instance.id)
            .exists()
        ):
            raise serializers.ValidationError(
                error_dict["already_exists"].format("Application name")
            )

        return value

    def validate_domain_name(self, value):
        """
        Validate that the domain name is unique for the user
        Args:
            value (str): The domain name
        Returns:
            str: The domain name
        Raises:
            serializers.ValidationError: If the domain name already exists
        """
        if (
            models.Application.objects.filter(
                domain_name=value, user=self.context["request"].user
            )
            .exclude(id=self.instance.id)
            .exists()
        ):
            raise serializers.ValidationError(
                error_dict["already_exists"].format("Domain name")
            )

        return value

    class Meta:
        model = models.Application
        fields = ("name", "description", "type", "framework", "domain_name")


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Plan
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class SubscriptionSerializer(serializers.ModelSerializer):
    application = serializers.PrimaryKeyRelatedField(
        queryset=models.Application.objects.all(),
        error_messages={
            "does_not_exist": error_dict["does_not_exist"].format("Application")
        },
    )
    plan = serializers.PrimaryKeyRelatedField(
        queryset=models.Plan.objects.all(),
        error_messages={"does_not_exist": error_dict["does_not_exist"].format("Plan")},
    )

    def validate_application(self, value):
        """
        Validate that the application belongs to the user
        Args:
            value (str): The application
        Returns:
            str: The application
        Raises:
            serializers.ValidationError: If the application does not belong to the user
        """
        if value.user != self.context["request"].user:
            raise serializers.ValidationError(
                error_dict["does_not_exist"].format("Application")
            )

        return value

    def validate(self, attrs):
        """
        Validate that the user has not already subscribed to the plan and application
        Args:
            attrs (dict): The attributes of the subscription
        Returns:
            dict: The attributes of the subscription
        Raises:
            serializers.ValidationError: If the user has already subscribed to the plan and application
        """
        if models.Subscription.objects.filter(
            plan=attrs["plan"],
            application=attrs["application"],
        ).exists():
            raise serializers.ValidationError(
                error_dict["already_exists"].format(
                    "Subscription to plan and application"
                )
            )

        return attrs

    class Meta:
        model = models.Subscription
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class SubscriptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
