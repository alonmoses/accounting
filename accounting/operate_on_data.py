
from store_data import Account

def calc_account_sum(transactions_list, account=None) -> float:
    sum = 0
    if not account:
        raise(ValueError("Missing account name to calculatte sum"))
    for transaction in transactions_list:
        if account not in transaction.get_attributes_list():
            raise(ValueError("Account name does not exist"))
        sum += getattr(transaction, account)

    return sum

def calc_transaction_net_income(transaction) -> float:
    net_income = 0
    transaction_data = transaction.get_transaction_data
    for account in transaction_data:
        if isinstance(transaction_data[account], Account):
            acc_amount = transaction_data[account].account_value
            acc_type = transaction_data[account].account_type
            net_income = net_income + acc_amount if acc_type == 'Assets' \
                else net_income - acc_amount

    return net_income
    
def calc_total_net_income(transactions_list) -> list:
    net_income_list = []
    for transaction in transactions_list:
        net_income_list.append(calc_transaction_net_income(transaction))

    return sum(net_income_list)
