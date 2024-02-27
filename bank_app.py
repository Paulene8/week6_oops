from bank_account import ChildBankAccount

def main():
    # Create a child bank account
    child_account = ChildBankAccount("123456789", 200, "Jane Doe")

    # Display initial details
    print("Account Number:", child_account.get_account_number())
    print("Initial Balance:", child_account.get_balance())
    print("Guardian Name:", child_account.guardian_name)

    # Perform transactions
    child_account.deposit(50)
    child_account.withdraw(100)

if __name__ == "__main__":
    main()
