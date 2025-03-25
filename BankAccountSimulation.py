#copilot ai 
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display_balance(self):
        print(f"Account balance: {self.balance}")

def main():
    account = BankAccount("John Doe", 1000)  # Initializing with an initial balance of 1000
    print(f"Welcome, {account.owner}!")

    while True:
        print("\nBank Account Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            account.display_balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
