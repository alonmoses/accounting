from dataclasses import dataclass, field
from currency_converter import CurrencyConverter
from typing import Dict


def get_currency_rate(val, currency) -> float:
    '''Convert input value from the givven currency to ILS '''
    _c = CurrencyConverter()
    return (_c.convert(val, currency, "ILS"))


@dataclass(frozen=True)
class Description:
    '''Class stores the description of the transaction'''
    transaction_index: int = 0
    description: str = ""

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


@dataclass(frozen=True)
class Month:
    pass




# @dataclass(frozen=True)
# class BeginBalance(Assets, Liabilities):
#     '''Class stores all the starting balance details of all accounts'''

#     def get_attributes_list(self):
#         return self.__dict__.keys()
