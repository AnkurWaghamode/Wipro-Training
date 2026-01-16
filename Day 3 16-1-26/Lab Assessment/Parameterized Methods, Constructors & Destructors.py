class BankAccount:
#Uses a parameterized constructor to initialize account_number and balance
   def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
        print("Bank account created successufully")
#Implements methods deposit(amount) and withdraw(amount)
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Deposited.Current Balance:{self.balance}")
        else:
            print("Invalid deposit amount")


    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawel amount")

        elif amount >self.balance:
            print("Insufficient Balance")

        else:
            self.balance -= amount
            print(f"Withdraw.Remaining Balance: {self.balance}")
#Uses a destructor to display a message when the object is deleted
    def __del__(self):
        print("Bank account obeject deleted")


account1 = BankAccount(101, 5000)
#Handle invalid withdrawal using proper checks
account1.deposit(2000)
account1.withdraw(1000)
account1.withdraw(7000)   # Invalid withdrawal

del account1
