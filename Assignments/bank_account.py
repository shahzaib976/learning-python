class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,money):
        self.balance+=money
        print("ADD MONEY       ==> ",money)
        
    def withdraw(self,money):
        self.balance-=money
        print("WITHDRAW MONEY  ==> ",money)

    def view_balance(self):
        print("---------------------------")
        if self.balance==0:
            print("No balance in your bank account")
            print()
        else:
            print("TOTAL BALANCE   ==> ",self.balance)
            print()
    


bank_Account = BankAccount("Noor",500000)
print('BALANCE         ==> ', bank_Account.balance)
bank_Account.deposit(5000)
bank_Account.deposit(10000)
bank_Account.deposit(4600)
bank_Account.deposit(3500)
bank_Account.deposit(56000)
bank_Account.withdraw(8000)
bank_Account.withdraw(4000)
bank_Account.withdraw(23900)
bank_Account.withdraw(54300)
bank_Account.view_balance()


bank_Account2 = BankAccount('Shahzaib',450000)
print('BALANCE         ==> ', bank_Account2.balance)
bank_Account2.deposit(3000)
bank_Account2.deposit(6000)
bank_Account2.deposit(6700)
bank_Account2.deposit(65000)
bank_Account2.deposit(3500)
bank_Account2.deposit(56000)
bank_Account2.withdraw(8000)
bank_Account2.withdraw(5000)
bank_Account2.view_balance()






        