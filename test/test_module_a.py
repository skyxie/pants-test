import pytest

from module_a import get_domain, plus_one


@pytest.mark.parametrize(
    "url,expected_domain",
    [
        ("https://google.com", "google"),
        ("https://whitehouse.gov", "whitehouse"),
        ("https://foo.us", "foo"),
    ],
)
def test_get_domain(url, expected_domain):
    assert get_domain(url) == expected_domain


@pytest.mark.parametrize(
    "x,y", [(1, 2), (-1, 0)]
)
def test_plus_one(x, y):
    assert plus_one(x) == y