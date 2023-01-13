import pytest

from module_a import get_domain


@pytest.mark.parameterize(
    "url,expected_domain",
    [
        ("https://google.com", "google"),
        ("https://whitehouse.gov", "whitehouse"),
        ("https://foo.us", "foo"),
    ],
)
def test_get_domain(url, expected_domain):
    assert get_domain(url) == expected_domain
