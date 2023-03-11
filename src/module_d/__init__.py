import requests

from module_a import plus_one


def plus_two(x: int) -> int:
    return plus_one(plus_one(x))


def get(url: str) -> int:
    return requests.get(url).status_code
