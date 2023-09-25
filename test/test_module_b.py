import pandas as pd
import pytest

from module_b import pretty_tables_params


def test_pretty_tables_params():
    df = pd.DataFrame(data={"foo": [1, 2], "bar": [3, 4]})
    result = pretty_tables_params(df, ["a", "b", "c", "d"])
    assert result["headers"] == ["foo", "bar"]
    assert result["rows"] == [[1, 3], [2, 4]]
    assert result["colors"] == ["a", "b"]

    with pytest.raises(RuntimeError) as e:
        pretty_tables_params(df, ["a"])
