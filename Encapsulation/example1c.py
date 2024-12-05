# TO provide more security implementing protection logic 
class BankAccount:
    def __init__(self,owner,balance,secret_key):
        self.owner=owner
        self.__balance=balance
        self.__secret_key=secret_key
    
    def __show_details(self):
        print("Account Owner:",self.owner)
        print("Acoount Balance:",self.__balance)
    def check_balance(self,provided_secret_key):
        if self.__secret_key==provided_secret_key:
            self.__show_details()
        else:
            print("invalid key")

    def get_balance(self):
        return self.__balance
    def set_balance(self,balance,provided_secret_key):
        if self.__secret_key==provided_secret_key:
            self.__balance=balance
        else:
            print("invalid key")
account=BankAccount("aksha",1000,"3456")
print("Account Balance:",account.get_balance())
account.set_balance(10000,"3456")
account.check_balance("3456")
#  now we giving access to attributes and methods in aresticted or controlled manner