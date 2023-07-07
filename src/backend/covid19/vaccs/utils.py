import pandas as pd


def get_locations_df() -> pd.DataFrame:
    df = pd.read_csv(
        "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/locations.csv")
    del df['iso_code']
    del df["source_website"]
    return df
