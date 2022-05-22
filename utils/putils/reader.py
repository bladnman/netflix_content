import pandas as pd
from mbmutils import mu
from ast import literal_eval


def read_titles() -> pd.DataFrame:
    df = pd.read_csv(mu.get_full_path("data/titles.csv"))

    # clean genres to be real lists
    df['genres'] = df['genres'].apply(literal_eval)

    # get year values into date object
    pd.to_datetime(df.release_year, format='%Y')

    # create decade values
    df["decade"] = (df.release_year//10)*10

    return df


def read_people() -> pd.DataFrame:
    df = pd.read_csv(mu.get_full_path("data/credits.csv"))
    return df
