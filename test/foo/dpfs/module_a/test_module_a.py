from module_a.dpfs import get_domain, plus_one


def test_get_domain():
    assert get_domain("https://google.com") == "google"
    assert get_domain("https://whitehouse.gov") == "whitehouse"
    assert get_domain("https://foo.us") == "foo"


def test_plus_one():
    assert plus_one(1) == 2
