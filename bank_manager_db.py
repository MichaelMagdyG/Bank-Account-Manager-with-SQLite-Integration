import sqlite3


class BankAccount:
    def __init__(self, account_holder, account_number, balance, account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount


class Bank:
    def __init__(self, db_name="bank.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            account_holder TEXT,
            balance REAL,
            account_type TEXT
        )
        """)
        self.conn.commit()

    def create_account(self, account_holder, account_number, initial_deposit, account_type):
        try:
            self.cursor.execute("""
            INSERT INTO accounts (account_number, account_holder, balance, account_type)
            VALUES (?, ?, ?, ?)
            """, (account_number, account_holder, initial_deposit, account_type))
            self.conn.commit()
            print("Account created successfully!")
        except sqlite3.IntegrityError:
            print("Account with this number already exists!")

    def list_accounts(self):
        self.cursor.execute("SELECT * FROM accounts")
        accounts = self.cursor.fetchall()
        return accounts

    def find_account(self, account_number):
        self.cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (account_number,))
        account = self.cursor.fetchone()
        if account:
            return BankAccount(*account[1:])
        else:
            raise ValueError("Account not found!")

    def update_account(self, account_number, balance):
        self.cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (balance, account_number))
        self.conn.commit()

    def close(self):
        self.conn.close()


def main():
    bank = Bank()
    while True:
        print("\nBank Account Manager")
        print("1. Create Account")
        print("2. View Accounts")
        print("3. Deposit Funds")
        print("4. Withdraw Funds")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                holder = input("Enter account holder name: ")
                number = input("Enter account number: ")
                deposit = float(input("Enter initial deposit: "))
                acc_type = input("Enter account type (Savings/Checking): ")
                bank.create_account(holder, number, deposit, acc_type)
            elif choice == "2":
                accounts = bank.list_accounts()
                for account in accounts:
                    print(f"Account Holder: {account[1]}, Account Number: {account[0]}, Balance: {account[2]}, Account Type: {account[3]}")
            elif choice == "3":
                number = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                account = bank.find_account(number)
                account.deposit(amount)
                bank.update_account(number, account.balance)
                print("Funds deposited successfully!")
            elif choice == "4":
                number = input("Enter account number: ")
                amount = float(input("Enter withdrawal amount: "))
                account = bank.find_account(number)
                account.withdraw(amount)
                bank.update_account(number, account.balance)
                print("Funds withdrawn successfully!")
            elif choice == "5":
                print("Goodbye!")
                bank.close()
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
