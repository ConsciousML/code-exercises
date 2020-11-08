import pandas as pd
import numpy as np


# 1. How to import pandas and check the version?
def import_pandas():
    import pandas as pd
    print(pd.__version__)

# 2. How to create a series from a list, numpy array and dict?
def obj_to_series(obj):
    return pd.Series(obj)

# 3. How to convert the index of a series into a column of a dataframe?

# Serie: a one dimensional object with axis label.
# DataFrame: two dimensional array, data structure containing labeled axes (rows and columns).

if __name__ == "__main__":
    array = np.zeros(10)
    lst = [i for i in range(10)]
    print(obj_to_series(array))
    print(obj_to_series(lst))