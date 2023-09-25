import math

import numpy as np
import pandas as pd

__version__ = "0.1.0"
__author__ = "Tian Xie <tian.xie@enigma.com>"


def get_counts() -> pd.DataFrame:
    s = pd.Series(np.random.normal(5, 1, 100)).map(math.floor)

    df = s.value_counts().reset_index()
    df.sort_values("index", inplace=True)
    return df
