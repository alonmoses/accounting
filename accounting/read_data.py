from store_data import Transaction
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


def extract_rows(dataframe) -> list():
    '''Read dataframe rows to create transaction list'''
    transactions_list = []
    head = dataframe.columns
    for _, row in dataframe.iterrows():
        transaction = Transaction()
        transaction.set_description(row[0:2])
        transaction.set_accounts(head, row[2:])
        transactions_list.append(transaction)

    return transactions_list
