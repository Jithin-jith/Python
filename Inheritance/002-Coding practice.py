#CHALLENGE
"""Bank Account System:

1. Create a base class BankAccount with attributes account_number and balance.
2. Add methods for deposit and withdrawal.
3. Create a derived class SavingsAccount that adds an interest rate and a method to calculate interest."""

#1. Create a base class BankAccount with attributes account_number and balance.
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    #2. Add methods for deposit and withdrawal. 
    def deposit(self,deposit_amount):
        self.balance = self.balance + deposit_amount
        return f"The remaining balance after depositing an amount of {deposit_amount} is {self.balance}"
    
    def withdraw(self,withdraw_amount):
        self.balance = self.balance - withdraw_amount
        return f"The remaining balance after withdrawing an amount of {withdraw_amount} is {self.balance}"
    
account1 = BankAccount('XXX1234',1500)
print(f"account number is {account1.account_number}")
print(f"account balance is {account1.balance}")

print(f"{account1.deposit(1200)}")
print(f"{account1.withdraw(700)}")

#3. Create a derived class SavingsAccount that adds an interest rate and a method to calculate interest.
class SavingsAccount(BankAccount):
    def __init__(self,account_number,balance,interest):
        super().__init__(account_number,balance)
        self.interest = interest
        
    def add_interest(self):
        return f"Amount after adding interset = {self.balance + self.balance * (self.interest/100)}"
    
sav_account = SavingsAccount(account_number="XX5678",balance=1000,interest=7)
print(f"Interest rate : {sav_account.interest}")
print(sav_account.add_interest())