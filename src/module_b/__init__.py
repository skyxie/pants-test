from typing import Any, Dict, List

import pandas as pd
import pretty_tables

from module_a import get_counts

COLORS = [
    pretty_tables.Colors.red,
    pretty_tables.Colors.green,
]


def pretty_tables_params(df: pd.DataFrame, colors: List[str]) -> Dict[str, Any]:
    headers = df.columns.to_list()
    if len(colors) < len(headers):
        raise RuntimeError("Need more colors!")
    return {
        "headers": headers,
        "rows": df.values.tolist(),
        "colors": colors[: len(headers)],
    }


def main(df: pd.DataFrame):
    print(pretty_tables.create(**pretty_tables_params(df, COLORS)))


if __name__ == "__main__":
    main(get_counts())
