class BankAccount():
    def __init__(self,account_number,balance,pin):
        self.account_number=account_number
        self.balance=balance
        self.__pin=pin             #pin attribute making as a private by adding __(underscore)

obj=BankAccount(122723090,2000,1029)
print(obj.balance)
print(obj.__pin)