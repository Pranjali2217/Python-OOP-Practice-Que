class BankAcount():
    def __init__(self,account_number,balance,pin):
        self.account_number=account_number
        self.balance=balance
        self.__pin=pin
    
    def deposite(self,amount):
        self.balance += amount
        print("deposited $",amount, "\n new balance: $",self.balance)

    def withdraw(self,cash,pin):
        if cash < self.balance and pin == self.__pin:
            self.balance -= cash
            print("amount withdraw sucsessfully")
        elif pin != self.__pin:
            print("wrong pin entered")
        elif cash > self.balance:
            print("insufficient amount")

cash=int(input("enter the amount: "))
obj=BankAcount(1297530203986,8000,1029)
obj.deposite(1000)
obj.withdraw(cash,1029)


        