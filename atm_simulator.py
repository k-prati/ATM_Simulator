class ATM:
    def __init__(self, balance=0, pin="1234"):
        # Initialize ATM with a starting balance and a default PIN
        self.balance = balance
        self.pin = pin
        self.transaction_history = []  # List to store transaction history

    def check_balance(self):
        # Display the current balance of the account
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append("Checked balance")  # Log the transaction

    def deposit(self, amount):
        # Add a specified amount to the account balance if it's valid
        if amount > 0:
            self.balance += amount
            print(f"You deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            self.transaction_history.append(f"Deposited ${amount:.2f}")  # Log the deposit
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        # Withdraw a specified amount if funds are sufficient and input is valid
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"You withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            self.transaction_history.append(f"Withdrew ${amount:.2f}")  # Log the withdrawal
        elif amount > self.balance:
            print("Insufficient balance. Please enter a smaller amount.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def change_pin(self, old_pin, new_pin):
        # Allow the user to change PIN if the old PIN matches
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("Changed PIN")  # Log the PIN change
        else:
            print("Incorrect old PIN. Please try again.")

    def show_transaction_history(self):
        # Display a list of all past transactions
        print("Transaction History:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def run(self):
        # Main loop to simulate ATM operations
        while True:
            print("\nATM Simulator")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")
            choice = input("Choose an option: ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                self.change_pin(old_pin, new_pin)
            elif choice == '5':
                self.show_transaction_history()
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    # Create an ATM instance with an initial balance of $500 and start the program
    atm = ATM(balance=500)
    atm.run()
