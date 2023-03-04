import tldextract

__version__ = "0.1.0"
__author__ = "Tian Xie <tian.xie@enigma.com>"


def get_domain(url: str) -> str:
    return tldextract.extract(url).domain


def plus_one(x: int) -> int:
    return x + 1
