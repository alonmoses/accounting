from operate_on_data import *

def get_income_statement(month):
    income_statement_str = ""
    income_statement_file = \
        f"../income_statements/{month.month}_statement.txt"

    transactions = month.get_month_transactions()
    income = calc_total_income(transactions)
    expenses = calc_total_expenses(transactions)

    accounts_list = month.get_accounts_list()
    accounts_begining_balance = month.get_accounts_begining_value()
    month_begining_balance = calc_begining_balance(accounts_begining_balance)

    head = f"Income Statement- {month.month}\n\n"
    begining_balance = f"Begining Balance: {int(month_begining_balance)}\n"
    income_statement_str += head
    income_statement_str += begining_balance
    for account in accounts_begining_balance:
        account_name = account.replace('\n', ' ')
        account_begining_balance = f"\t{account_name}: {int(accounts_begining_balance[account])}\n"
        income_statement_str += account_begining_balance

    total_income = f"\nIncome: {int(income)}\n"
    income_statement_str += total_income

    total_expenses = f"\nExpenses: {int(expenses)}\n"
    income_statement_str += total_expenses
    for account in accounts_begining_balance:
        account_name = account.replace('\n', ' ')
        expenses_dict = calc_account_expense(transactions, account)
        if expenses_dict['total_expense'] == 0: continue
        account_expenses = f"\t{account_name}: {int(expenses_dict['total_expense'])}\n"
        income_statement_str += account_expenses
        for expense_type in expenses_dict:
            if expenses_dict[expense_type] != 0 and expense_type != 'total_expense':
                per_type_account_expenses = f"\t\t({int(expenses_dict[expense_type])}){expense_type}\n"
                income_statement_str += "{left_aligned:^10}".format(left_aligned=per_type_account_expenses)
            
        
    with open(income_statement_file, "w",  encoding='utf-8') as f:
        f.write(income_statement_str)

    
    return income_statement_str