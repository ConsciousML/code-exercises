import pandas as pd

# Read csv with Pandas
def read_csv(path):
    return pd.read_csv(path)

# Concatenating two data frames with same columns
def concate_dfs(df_0, df_1):
    return pd.concat([df_0, df_1], axis=0)

# Creating a new column
def add_col_df(df, pd_serie, col_name):
    df['new_column'] = pd_serie
    return df

# Delete a column
def drop_cols(df, col_names)
    return df.drop(columns=col_names)