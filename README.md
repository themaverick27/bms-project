# 🏦 Bank Management System

A simple **Bank Management System built with Python and Object-Oriented Programming (OOP)**.

This project demonstrates core Python concepts such as **classes, objects, class variables, class methods, instance methods, file handling, JSON persistence, conditional statements, list comprehensions, and basic exception handling**.

The application stores account information in a local `JSON` file instead of using a database.

## 📌 Features

The application currently supports:

* 🏦 Create a new bank account
* 💰 Deposit money
* 💸 Withdraw money
* 👤 View bank account details
* ✏️ Update account details
* 🗑️ Delete a bank account
* 💾 Persistent data storage using JSON
* 🔐 Account verification using account number and PIN
* 🎲 Automatic account number generation


## 🛠️ Tech Stack

* **Python**

## 📂 Project Structure

```text
bms-project/
│
├── main.py
├── data.json
└── README.md
```

### `main.py`

Contains the complete Bank Management System implementation.

### `data.json`

Used as a local storage file for saving bank account information.

Example:

```json
[
    {
        "name": "John Doe",
        "age": 25,
        "email": "john@example.com",
        "pin": 1234,
        "accountNum": "A7x3!B9",
        "balance": 5000
    }
]
```

## 💾 Data Persistence

Instead of using a traditional database such as MySQL or MongoDB, this project uses a local JSON file.

Whenever an account is:

* Created
* Updated
* Deposited into
* Withdrawn from
* Deleted

the updated data is written back to:

```text
data.json
```

This allows the data to remain available even after the program is closed.

## 🔄 Application Flow

```text
Start Application
       │
       ▼
   Bank Object
       │
       ▼
   Display Menu
       │
       ├── 1. Create Account
       │
       ├── 2. Deposit Money
       │
       ├── 3. Withdraw Money
       │
       ├── 4. Bank Details
       │
       ├── 5. Update Details
       │
       └── 6. Delete Account
```

## ⚠️ Note:

This project is intended for **learning Python and OOP**, not for real banking use.

---
