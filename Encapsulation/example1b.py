# to Access private Attributes we use Getter And Setter Methods
# Getter:which is a public method to access the private Attributes
# Setter:which is a public method to modify the private attributes
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    
    def show_details(self):
        print("Account Owner:",self.owner)
        print("Acoount Balance:",self.__balance)

    def get_balance(self):
        return self.__balance
    def set_method(self,balance):
        self.__balance=balance
account=BankAccount("aksha",1000)
print("Account Balance:",account.get_balance())
account.self_balance(1888)
print("Account Balance:",account.get_balance())