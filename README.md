# 🏦 Bank Management System (Python)

## 📌 Overview

This is a simple **Bank Management System** implemented in Python using Object-Oriented Programming (OOP).
It allows users to perform basic banking operations such as:

* Viewing account details
* Depositing (crediting) money
* Withdrawing (debiting) money
* Setting and verifying a PIN

---

## ⚙️ Features

### 🔹 Account Management

* Create an account with:

  * Name
  * Account ID
  * Initial balance
  * PIN

### 🔹 Transactions

* **Debit (Withdraw Money)**

  * Checks for sufficient balance
  * Requires correct PIN

* **Credit (Deposit Money)**

  * Adds money to account
  * Validates input

### 🔹 Security

* PIN-based authentication for transactions

### 🔹 Additional Options

* View account details
* Change PIN
* Menu-driven interface

---

## 🧱 Class Structure

### `Bank` Class

Contains:

* **Attributes:**

  * `account_name`
  * `account_Id`
  * `account_balance`
  * `account_pin`

* **Methods:**

  * `showdetails()` → Displays account info
  * `debit(amount)` → Withdraws money
  * `credit(amount)` → Deposits money
  * `set_pin(pin)` → Updates PIN
  * `check_pin(pin)` → Verifies PIN
  * `showoptions()` → Displays menu

---

## ▶️ How to Run

1. Install Python (3.x recommended)
2. Save the script as `bank.py`
3. Run the program:

```bash
python bank.py
```

---

## 💻 Sample Usage

```
Enter name: John
Enter account Id: 12345
Enter balance: 5000
Enter PIN: 1111

Transaction options:-
Enter 1 to Debit
Enter 2 to Credit
Enter 3 to Show Your Account Details
Enter 4 to Set New PIN
Enter 5 to Exit
```

---

## 📄 License

This project is open-source and free to use for learning purposes.

---

## 🙌 Author

Developed as a beginner-friendly Python OOP project.
