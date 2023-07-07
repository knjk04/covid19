from rest_framework import serializers

from .models import Country, Source, Vaccine


class VaccineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vaccine
        fields = ["name"]


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    source = serializers.StringRelatedField()
    vaccine = serializers.StringRelatedField(many=True)
    class Meta:
        model = Country
        fields = ["name", "last_updated", "source", "vaccine"]


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ["name"]
