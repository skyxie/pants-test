import requests

from module_b import plus_y


def times_two(x: int) -> int:
    return plus_y(x, x)


def get(url: str) -> int:
    return requests.get(url).status_code
