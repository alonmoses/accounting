import pandas as pd
from functools import wraps

def replace_nan_with_zero(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        dataframe = func(*args, **kwargs)
        dataframe.fillna(0, inplace=True)
        return dataframe
    return wrapper

@replace_nan_with_zero
def read_excel(file_name, header=[0,1,2,3]):
    df = pd.read_excel(file_name, header)
    return df

@replace_nan_with_zero
def read_excel_sheet(file_name, sheet_name, header=[0,1,2,3]):
    df = pd.read_excel(file_name, sheet_name, header)
    return df


