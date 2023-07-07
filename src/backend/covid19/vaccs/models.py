from django.db import models

# Domain model for https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/locations.csv


class Vaccine(models.Model):
    """
    Name of a vaccine (e.g. Pfizer/BioNTech)
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Source(models.Model):
    """
    Where the information has come from (e.g. World Health Organization)
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=60, unique=True)
    last_updated = models.DateField()
    vaccine = models.ManyToManyField(Vaccine)
    source = models.OneToOneField(Source, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}, Last updated: {self.last_updated}, Source: {self.source}"
