class BankAccount:
    def __init__(self,account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

            print(f"Deposited {amount}.New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount

                print(f"withdrew{amount}. New balance is {self.balance}.")

            else:
                print("withdrawal amount must be positive.")

    def get_balance(self):
        print(f"Current balance is {self.balance}.")
        return self.balance

    def display_details(self):
        print(f"Account Number:{self.account_number}")
        print(f"Account Holder:{self.account_holder}")
        print(f"Balance:{self.balance}")

#Examble usage:
account = BankAccount("123456789", "john Doe",1000.0)

#Deposit money
account.deposit(500)

#withdraw money
account.withdraw(400)

#check balance
account.get_balance()

#Display account details
account.display_details()
