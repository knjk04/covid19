from django.http import HttpResponse
from rest_framework import viewsets

from .models import Country
from .serializers import CountrySerializer


def index(request):
    return HttpResponse(Country.objects.all())


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
