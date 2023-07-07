import pandas as pd
from django.db.utils import IntegrityError
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Country, Source, Vaccine
from .serializers import CountrySerializer
from .utils import get_locations_df


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


@api_view(["POST"])
def ingest(request):
    for row in get_locations_df().itertuples():
        vaccines = row.vaccines.split(", ")
        for v in vaccines:
            try:
                Vaccine(name=v).save()
                print(f"Saved {v}...")
            except IntegrityError:
                print(f"{v} exists")

        s = Source(name=row.source_name)
        try:
            s.save()
            print(f"Saved {row.source_name}")
        except IntegrityError:
            print(f"{row.source_name} exists")

        print()

    return Response(status=status.HTTP_200_OK)
