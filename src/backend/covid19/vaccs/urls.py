from django.urls import include, path
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'countries', views.CountryViewSet)

urlpatterns = [
    # path("", views.index, name="index")
    path("", include(routers.urls)),
    path("api", include("rest_framework.urls", namespace="rest_framework"))
]
