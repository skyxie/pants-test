import pandas as pd

from module_a import get_counts


def get_proportions() -> pd.DataFrame:
    df = get_counts()

    val_col = next(c for c in df.columns if c != "index")
    total = df[val_col].sum()
    return df.assign(percent=df[val_col] / total)
