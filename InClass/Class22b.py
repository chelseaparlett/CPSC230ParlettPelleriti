Bank_Customer = {"name": "Ashleigh", "balance": 2000, "status": "Silver"}

def withdraw(Bank_Customer, amount):
    Bank_Customer["balance"] -= amount
def deposit(Bank_Customer, amount):
    Bank_Customer['balance'] += amount
def get_balance(Bank_Customer):
    print(Bank_Customer['balance'])
    return Bank_Customer['balance']
def set_status(Bank_Customer):
    if Bank_Customer['balance'] >1000000:
        Bank_Customer['status'] = "Gold"
    elif Bank_Customer['balance'] > 100000:
        Bank_Customer = "Silver"
    else:
        Bank_Customer['balance'] = "Bronze"
    print("your new status is " + Bank_Customer['status'])


class Bank_Customer():
    def __init__(self,name, balance, status):
        self.name = name
        self.wealth = balance
        self.status = status
        print("Welcome")
    def withdraw(self, amount):
        self.wealth -= amount
        return amount
    def deposit(self, amount):
        self.wealth += amount
    def get_balance(self):
        print(self.wealth)
        return self.wealth
    def set_status(self):
        if self.wealth >1000000:
            self.status = "Gold"
        elif self.wealth > 100000:
            self.status = "Silver"
        else:
            self.wealth = "Bronze"
        print("your new status is " + self.status)

Joe = Bank_Customer("Joe", 100000000, "Gold")
print(Joe.name)
cash = Joe.withdraw(10)
print(cash)
