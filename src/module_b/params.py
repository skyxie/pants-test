from typing import Any, Dict, List
import pandas as pd


def pretty_tables_params(df: pd.DataFrame, colors: List[str]) -> Dict[str, Any]:
    headers = df.columns.to_list()
    if len(colors) < len(headers):
        raise RuntimeError("Need more colors!")
    return {
        "headers": headers,
        "rows": df.values.tolist(),
        "colors": colors[: len(headers)],
    }
