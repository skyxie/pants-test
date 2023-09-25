from module_c import get_proportions


def test_column_names():
    df = get_proportions()
    cols = df.columns.to_list()
    assert "index" in cols
    assert 0 in cols
    assert "percent" in cols
