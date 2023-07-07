from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

routers = routers.DefaultRouter()
routers.register(r'countries', views.CountryViewSet)

urlpatterns = [
    path("", include(routers.urls)),
    path("api", include("rest_framework.urls", namespace="rest_framework")),
    path("ingest", views.ingest)
]

# urlpatterns = format_suffix_patterns(urlpatterns)
