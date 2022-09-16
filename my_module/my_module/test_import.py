import pandas as pd


def add_one(df: pd.DataFrame):
    df.loc["b", ":"] = df["a"] + 1
    return df
