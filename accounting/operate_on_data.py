
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

def calc_transaction_net_worth(transaction) -> float:
    net_income = 0
    transaction_data = transaction.get_transaction_data
    for account in transaction_data:
        if isinstance(transaction_data[account], Account):
            acc_amount = transaction_data[account].account_value
            acc_type = transaction_data[account].account_type
            net_income = net_income + acc_amount if acc_type == 'Assets' \
                else net_income - acc_amount

    return net_income
    
def calc_total_expenses(transactions_list) -> float:
    expenses_list = []
    for transaction in transactions_list:
        expenses_list.append(calc_transaction_net_worth(transaction))

    return sum(expenses_list)

def calc_account_expense(transactions_list, account_name) -> float:
    total_expense = 0
    for transaction in transactions_list:
        transaction_data = transaction.get_transaction_data
        try:
            total_expense += transaction_data[account_name].account_value
        except:
            raise(KeyError(f"{account_name} is not a valid account"))

    return total_expense

def calc_begining_balance(accounts_begining_dict) -> float:
    begining_balance = sum(val for _,val in accounts_begining_dict.items())
    return begining_balance

def calc_total_net_income(month) -> float:
    begining_balance = calc_begining_balance(month.get_accounts_begining_value())
    total_expenses = calc_total_expenses(month.get_month_transactions())
    return begining_balance + total_expenses

