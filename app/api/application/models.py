from django.contrib.auth import get_user_model
from django.db import models

from ..helpers.constants import APP_FRAMEWORK_CHOICES, APP_TYPE_CHOICES

User = get_user_model()


class Application(models.Model):
    """
    An application is a collection of code that is deployed to a platform.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, choices=APP_TYPE_CHOICES)
    framework = models.CharField(max_length=255, choices=APP_FRAMEWORK_CHOICES)
    domain_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        User, related_name="applications", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        unique_together = ("name", "user")

    def __str__(self):
        return self.name


class Plan(models.Model):
    """
    A plan is a subscription plan that can be associated with an application.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Plan"
        verbose_name_plural = "Plans"

    def __str__(self):
        return self.name


class Subscription(models.Model):
    """
    A subscription is a record of what plan is associated with an application.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    plan = models.ForeignKey(
        Plan, related_name="subscriptions", on_delete=models.CASCADE
    )
    application = models.ForeignKey(
        Application, related_name="subscriptions", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __str__(self):
        return f"{self.application.name} - {self.plan.name}"
