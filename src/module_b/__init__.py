import pandas as pd
import pretty_tables

from module_a import get_counts

from .params import pretty_tables_params
from .colors import COLORS


def main(df: pd.DataFrame):
    print(pretty_tables.create(**pretty_tables_params(df, COLORS)))


if __name__ == "__main__":
    main(get_counts())
