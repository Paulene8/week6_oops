class BankAccount:
    def __init__(self, account_number, balance=0):
        # __init__: This is the constructor method when a new instance of the class is created. It
        # initializes the attributes account_number and balance. The balance is set to a default value of 0
        self._account_number = account_number
        # Encapsulation using underscore to denote private attribute
        self._balance = balance

    # Getters and setters are methods used to access (get) and modify (set) the attributes of an object
    # Getter method for account number
    def get_account_number(self):
        return self._account_number

    # Setter method for balance
    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Insufficient balance")

    # Getter method for balance
    def get_balance(self):
        return self._balance

    # deposit is a method to add money to the bank account
    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount should be positive.")

    # method for money withdrawal
    def withdraw(self, amount):
        # logic to check if the balance is enough for withdrawal
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid amount or insufficient funds.")


# ChildBankAccount class inheriting from BankAccount
class ChildBankAccount(BankAccount):
    def __init__(self, account_number, balance=0, guardian_name=""):
        super().__init__(account_number, balance)  # Call to superclass constructor using super()
        self.guardian_name = guardian_name  # Public attribute without _

    # Decorator to define guardian_name as a property
    @property
    def guardian_name(self):
        return self._guardian_name

    # Setter for guardian_name
    @guardian_name.setter
    def guardian_name(self, name):
        self._guardian_name = name
