import pandas as pd
import pretty_tables

from module_b.params import pretty_tables_params
from module_c import get_proportions

COLORS = [
    pretty_tables.Colors.yellow,
    pretty_tables.Colors.cyan,
    pretty_tables.Colors.purple,
]


def main(df: pd.DataFrame):
    print(pretty_tables.create(**pretty_tables_params(df, COLORS)))


if __name__ == "__main__":
    main(get_proportions())
