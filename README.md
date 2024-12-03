
# Bank Account Manager with Database Integration

This project is a console-based Bank Account Manager application built in Python with SQLite database integration. It showcases advanced programming concepts like Object-Oriented Programming (OOP), database handling, and persistent storage.

## Features

1. **Create Account**: Add a new bank account with details like holder name, account number, initial deposit, and account type (e.g., Savings or Checking).
2. **View Accounts**: Display a list of all accounts with their details.
3. **Deposit Funds**: Add money to an existing account, with updates reflected in the database.
4. **Withdraw Funds**: Deduct money from an account (ensuring sufficient balance), with updates reflected in the database.
5. **Persistent Storage**: Data is stored in an SQLite database (`bank.db`) for future use.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bank-account-manager.git
   cd bank-account-manager
   ```

2. Ensure Python 3.x is installed on your system.

3. Install SQLite (if not already installed). SQLite is usually included with Python installations.

## Usage

Run the program from the terminal or command prompt:

```bash
python bank_manager_db.py
```

Follow the on-screen menu to perform operations like creating accounts, viewing account details, or managing transactions.

## Example Output

### Sample Menu:
```
Bank Account Manager
1. Create Account
2. View Accounts
3. Deposit Funds
4. Withdraw Funds
5. Exit
Enter your choice:
```

### Sample Account Data in Database:
| Account Number | Account Holder | Balance | Account Type |
|----------------|----------------|---------|--------------|
| 123456789      | John Doe       | 1000.0  | Savings      |
| 987654321      | Jane Smith     | 500.0   | Checking     |

## Future Enhancements

- Add transaction history for each account.
- Implement PIN verification for secure account access.
- Enhance the user interface with a graphical or web-based front end.
- Expand database functionality with advanced queries and analytics.

## Screenshots
<div align="center">
  <img src="Screenshot%202024-12-03%20153907.jpg" alt="Bank Account Manager with SQLite Integration Screenshot">
</div>
