# To restrict the access to attributes and methods of a class from outside the class we use private and public access modifiers: 
# private access modifiers
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    
    def show_details(self):
        print("Account Owner:",self.owner)
        print("Acoount Balance:",self.__balance)

account=BankAccount("aksha",1000)
account.show_details()
account.__balance+=1000

