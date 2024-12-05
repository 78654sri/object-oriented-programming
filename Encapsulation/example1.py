class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def show_details(self):
        print("Account Owner:",self.owner)
        print("Acoount Balance:",self.balance)

account=BankAccount("aksha",1000)
account.show_details()
print(account.owner)
print(account.balance)
account.balance+=1000
print(account.balance)
account.owner="helo"
print(account.owner)
print(account.balance)
#when I am trying to modify and access Account details outside the class they will get modified and accessed.so now there is no protection for bankaccount data.