
"""
2. Create a Bank account with members account number, name, type of account and balance.
Write constructor and methods to deposit at the bank and withdraw an amount from the bank.
"""
class Bankaccount:
    def __init__(self):
        self.balance=0
        print("\n Account is created ")    
    def deposit(self,amt):
        self.balance=self.balance+amt
        self.currnet_balance()

    def withdraw(self,amt):
        if (self.balance>=amt):
            self.balance=self.balance-amt
            self.currnet_balance()
        else:
            print("Insufficient Balance")
    
    def currnet_balance(self):
        print("\n Your Current Balance is :",self.balance)
account=Bankaccount()
cnt=True
while(cnt):
    ch=int(input("\n press 1 for deposite \n \
                    2 for withdraw \n \
                    3 for check balance \n \
                    4 for quit "))
    if ch==1:
        amount=int(input("\n enter amount to deposit"))
        account.deposit(amount)
        ch=0
    if ch==2:
        amount=int(input("\n enter amount to withdraw"))
        account.withdraw(amount)
        ch=0
    if ch==3:
        account.currnet_balance()
        ch=0
    if ch==4:
        cnt=False


