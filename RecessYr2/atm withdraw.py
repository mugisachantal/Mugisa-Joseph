class ATM:
    """
    A simple ATM simulator class.
    Manages user login and withdrawal operations.
    """

    def __init__(self, initial_balance=1000.00, correct_pin="1234"):
        """
        Initializes the ATM with a default balance and PIN.

        Args:
            initial_balance (float): The starting balance for the account.
            correct_pin (str): The correct PIN for login.
        """
        self.balance = initial_balance
        self.correct_pin = correct_pin
        self.is_logged_in = False
        print("ATM initialized. Default balance: ${:.2f}".format(self.balance))

    def login(self):
        """
        Simulates the login process.
        Prompts the user for a PIN and validates it.
        """
        if self.is_logged_in:
            print("You are already logged in.")
            return

        attempts = 0
        max_attempts = 3
        while attempts < max_attempts:
            entered_pin = input("Please enter your PIN: ")
            if entered_pin == self.correct_pin:
                self.is_logged_in = True
                print("Login successful! Welcome.")
                return True
            else:
                attempts += 1
                print(f"Invalid PIN. You have {max_attempts - attempts} attempts remaining.")
        print("Too many failed attempts. Your card has been blocked.")
        return False

    def withdraw(self):
        """
        Simulates the withdrawal process.
        Prompts for an amount, checks balance, and processes withdrawal.
        """
        if not self.is_logged_in:
            print("Please log in first to perform a withdrawal.")
            return

        print(f"Your current balance is: ${self.balance:.2f}")
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                self.balance -= amount
                print(f"Successfully withdrew ${amount:.2f}.")
                print(f"New balance: ${self.balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    def check_balance(self):
        """Displays the current account balance."""
        if not self.is_logged_in:
            print("Please log in first to check your balance.")
            return
        print(f"Your current balance is: ${self.balance:.2f}")

    def logout(self):
        """Logs out the user."""
        if self.is_logged_in:
            self.is_logged_in = False
            print("You have been logged out. Goodbye!")
        else:
            print("You are not currently logged in.")

    def run(self):
        """
        Runs the main ATM simulation loop.
        Allows the user to perform various operations until they exit.
        """
        print("\n--- Welcome to the Simple Python ATM ---")

        if not self.login():
            print("Exiting ATM due to login failure.")
            return

        while self.is_logged_in:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Logout")
            print("4. Exit ATM (without logging out)")
            choice = input("Please choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.logout()
            elif choice == '4':
                print("Thank you for using the ATM. Exiting...")
                break # Exit the while loop
            else:
                print("Invalid choice. Please try again.")

# --- Main execution block ---
if __name__ == "__main__":
    my_atm = ATM() # Create an instance of the ATM
    my_atm.run()   # Start the ATM simulation
