"""app URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views

urlpatterns = [
    path(
        "",
        views.ApplicationCreateListView.as_view(),
        name="application-create-list",
    ),
    path(
        "<int:pk>/",
        views.ApplicationRetrieveUpdateDestroyView.as_view(),
        name="application-retrieve-update-destroy",
    ),
    path(
        "plans/",
        views.PlanListView.as_view(),
        name="plan-list",
    ),
    path(
        "plans/<int:pk>/",
        views.PlanRetrieveView.as_view(),
        name="plan-retrieve",
    ),
    path(
        "subscriptions/",
        views.SubscriptionCreateListView.as_view(),
        name="subscription-create-list",
    ),
    path(
        "subscriptions/<int:pk>/",
        views.SubscriptionRetrieveUpdateView.as_view(),
        name="subscription-retrieve-update",
    ),
]
