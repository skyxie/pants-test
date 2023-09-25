import pandas as pd

from module_a import get_counts


def test_column_names():
    df = get_counts()
    cols = df.columns.to_list()
    assert "index" in cols
    if pd.__version__.startswith("2"):
        assert "count" in cols
    else:
        assert 0 in cols
