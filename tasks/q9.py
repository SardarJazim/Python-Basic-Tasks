class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Current balance for {self.account_holder}: ${self.balance}")

def display_menu():
    print("WELCOME")
    print("Choose an operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")

def get_user_choice():
    return input("Enter your choice (1-3): ")

if __name__ == "__main__":
    account1 = BankAccount("JAZIM ", initial_balance=1000)
display_menu()
choice = get_user_choice()
if choice == '1':
            amount = float(input("Enter the deposit amount: "))
            account1.deposit(amount)
elif choice == '2':
            amount = float(input("Enter the withdrawal amount: "))
            account1.withdraw(amount)
elif choice == '3':
            account1.display_balance()
else:
            print("Invalid choice. Please enter a number between 1 and 3.")
