from dataclasses import dataclass, field
from currency_converter import CurrencyConverter
from read_data import read_excel_sheet


def get_currency_rate(val, currency) -> float:
    '''Convert input value from the givven currency to ILS '''
    _c = CurrencyConverter()
    return (_c.convert(val, currency, "ILS"))


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


@dataclass(frozen=True)
class Account:
    account_type: str
    account_value: float = 0.0


@dataclass(frozen=True)
class Transaction:
    '''Class stores all the transaction's details to have complete
    information of it'''
    transaction_data: dict = field(default_factory=dict)

    def set_description(self, data):
        self.transaction_data['Transaction #'] = data[0]
        self.transaction_data['Description'] = data[1]

    def set_accounts(self, head, data):
        for idx, account in enumerate(head[2:]):
            _type = account[0]
            _name = account[1]
            _value = get_currency_rate(data[idx] ,'USD') if '$' in _name \
                 else data[idx]

            self.transaction_data[_name] = Account(account_type=_type, \
                account_value=_value)

    @property
    def get_transaction_data(self):
        return self.transaction_data


@dataclass
class Month:
    month: str
    xlsx_path: str
    _transactions_list: list = field(init=False)
    _accounts_list: list = field(default_factory=list)
    _account_begining: dict = field(default_factory=dict)

    def __post_init__(self):
        self._dataframe = read_excel_sheet(self.xlsx_path, self.month)
        self.set_month_transactions()
        self.set_accounts_begining_value()

    def set_month_transactions(self):
        self._transactions_list = extract_rows(self._dataframe)
    
    def get_month_transactions(self):
        return self._transactions_list

    def set_accounts_begining_value(self):
        for col in self._dataframe.head(0):
            accont_type, account, value, _ = col
            if accont_type in ['Assets', 'Liabilities'] \
                 and value != '-': #isinstance(value, float):
                if '$' in account: value = get_currency_rate(value, 'USD')
                self._account_begining[account] = value
                self._accounts_list.append(account)

    def get_accounts_begining_value(self):
        return self._account_begining

    def get_accounts_list(self):
        return self._accounts_list

        



