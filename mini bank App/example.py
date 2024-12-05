class Customer:
    "this class develop by vysh"
    bank_name="vyshBank"
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    
    def deposite(self,amount):
        self.balance += amount
        print(f"deposite {amount} to {self.name} account")

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print("after withdrw:",self.balance)
print("welcome to",Customer.bank_name)
name=input("enter your name:")
c=Customer(name)

while True:
    print("\n1.deposite\n2.withdraw\n3.exit")
    ch=int(input("enter your choice:"))
    if ch=="1":
        amount=int(input("enter amount:"))
        c.deposite(amount)
    elif ch=="2":
        amount=int(input("enter amount:"))
        c.withdraw(amount)
    else:
        print("THanks for banking")
        break

    