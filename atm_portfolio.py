class ATMMachine:
    def __init__(self):
        self.state = 'Idle'
        self.pin_attempts = 0
        self.MAX_PIN_ATTEMPTS = 3
        self.account_balance = 500  # Example of balance

    def insert_card(self):
        print("Please insert your card.")
        self.state = 'Authentication'
        self.authenticate_user()

    def authenticate_user(self):
        print("ATM prompts user to enter PIN.")
        for _ in range(3):  # Simulating up to three attempts
            pin = input("Enter your PIN: ")
            if self.check_pin(pin):
                print("PIN is correct.")
                self.state = 'MainMenu'
                self.show_main_menu()
                return
            else:
                self.pin_attempts += 1
                print("Incorrect PIN, please try again.")
                if self.pin_attempts >= self.MAX_PIN_ATTEMPTS:
                    self.eject_card("Too many incorrect attempts")
                    return
        self.state = 'Idle'

    def check_pin(self, pin):
        # how normally you would validate with the bank's authentication server
        correct_pin = "1234"  # Example PIN
        return pin == correct_pin

    def show_main_menu(self):
        print("ATM displays Main Menu.")
        print("1. Withdraw Cash")
        choice = input("Select an option: ")
        if choice == '1':
            if self.account_balance > 0:
                self.withdraw_cash()
            else:
                print("Account is closed.")
                self.eject_card()
                self.state = 'Idle'

    def withdraw_cash(self):
        self.state = 'Withdrawal'
        self.select_amount()

    def select_amount(self):
        print("ATM presents default quantities and custom amount option.")
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= self.account_balance:
            self.dispense_cash(amount)
        else:
            print("Insufficient funds.")
            self.show_main_menu()

    def dispense_cash(self, amount):
        self.account_balance -= amount
        print(f"ATM dispenses ${amount}.")
        print(f"New account balance: ${self.account_balance}")
        self.print_receipt(amount)
        self.eject_card()

    def print_receipt(self, amount):
        print(f"Receipt: Withdrawn: ${amount}, Remaining balance: ${self.account_balance}")

    def eject_card(self, message=""):
        if message:
            print(message)
        print("Thank you, please take your card.")
        self.state = 'Idle'

# Example usage
atm = ATMMachine()
atm.insert_card()
