import pandas as pd
import numpy as np


# 1. How to import pandas and check the version?
def import_pandas():
    import pandas as pd
    print(pd.__version__)

# 2. How to create a series from a list, numpy array and dict?
def obj_to_series(obj):
    return pd.Series(obj)

# 3. How to convert series into a dataframe?
def serie_to_df(serie):
    return serie.to_frame()

# Serie: a one dimensional object with axis label.
# DataFrame: two dimensional array, data structure containing labeled axes (rows and columns).
# def series_to_column(serie, df):



if __name__ == "__main__":
    serie = pd.Series([i for i in range(10)])
    print(serie.to_frame().reset_index())