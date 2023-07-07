import pandas as pd
from models import Source

df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv")
del df['iso_code']
del df["source_website"]

countries = set()
for row in df.itertuples():
    s = Source(name=row.source_name)
    s.save()
    if row.location not in countries:
        countries.add(row.location)

for c in countries:
    print(c)
