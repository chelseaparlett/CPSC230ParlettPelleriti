# #--------------------------------------
# Bank_Customer = {"name": "Ashleigh",
#  "balance": 2000, "status": "Silver"}
#
# def withdraw(bc,amnt):
#     bc["balance"] -= amnt
#     return(bc)
# def deposit(bc, amnt):
#     bc["balance"] += amnt
#     return(bc)
# def get_balance(bc):
#     #a = bc["balance"]
#     print(bc["name"] + " your balance is " + str(bc["balance"]))
# #--------------------------------------
# Bank_Customer = {"name": "Ashleigh", "balance": 2000, "status": "Silver"}
#
# def withdraw(Bank_Customer, amount):
#     Bank_Customer["balance"] -= amount
# def deposit(Bank_Customer, amount):
#     Bank_Customer['balance'] += amount
# def get_balance(Bank_Customer):
#     print(Bank_Customer['balance'])
#     return Bank_Customer['balance']
# def set_status(Bank_Customer):
#     if Bank_Customer['balance'] >1000000:
#         Bank_Customer['status'] = "Gold"
#     elif Bank_Customer['balance'] > 100000:
#         Bank_Customer = "Silver"
#     else:
#         Bank_Customer['balance'] = "Bronze"
#     print("your new status is " + Bank_Customer['status'])


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
print(Joe.wealth)
cash = Joe.withdraw(10)
print(Joe.wealth)
#print(cash)

class list():
    def sort():


chardict = {"raul": {"sp": {}}, "xm" :{}}
powerdict = {"raul": {}}
print(chardict.keys())
choice = input("Which of the above do you want? ")
playerHuman = chardict[choice]
c = chardict.keys()
c.remove(choice)
comp = random.choice(c)
opponentComputer =  chardict[comp]

while response.lower() not in ["special attack", "basic attack"]:
    reponse = input()

def attack(attacker,attackee,sp = False):
    if sp:
        damage = random.randint(attacker["sp"]["range"][0],attacker["sp"]["range"][1])

    else:
        do baic stuff

attack(me,them,True)
attack(them,me,False)
