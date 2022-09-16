import pandas as pd
from my_module.test_import import add_one

__version__ = "0.1.0"
__author__ = "Tian Xie <tian.xie@enigma.com>"


def main():
    df = pd.createDataFrame({"a": [1, 2]})
    df = add_one(df)
    print(df.to_string())


if __name__ == "__main__":
    main()
