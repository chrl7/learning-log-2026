# Simple Finance Tracker

Capstone project for the **Object-Oriented Programming (OOP)** module — part of [`learning-log-2026`](../../README.md).

A simple CLI program to record financial transactions (income & expenses), calculate balance, validate input, and persist transaction history to a CSV file.

---

## Features

- Record **Revenue** and **Expenditure** transactions
- Display transaction history with a distinct format for each type
- Automatically calculate balance (total revenue − total expenditure)
- Built-in validation:
  - Transaction amount must be greater than 0 (`InvalidAmount`)
  - Expenditures cannot exceed the available balance (`InsufficientBalance`)
- Save transaction history to a `.csv` file
- Reload transaction history on program restart (persistent data)

---

## OOP Concepts Applied

| Concept              | Implementation in Project                                                                             |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| **Class & Object**   | `Transaction`, `Wallet` as the core entities                                                          |
| **Inheritance**      | `Revenue` and `Expenditure` inherit from `Transaction`                                                |
| **Polymorphism**     | `show()` method overridden differently in `Revenue` vs `Expenditure`, called uniformly through a loop |
| **Composition**      | `Wallet` **has** many `Transaction` objects (has-a), distinct from inheritance (is-a)                 |
| **Custom Exception** | `InvalidAmount`, `InsufficientBalance` — inherit from Python's built-in `Exception`                   |
| **Error Handling**   | `try-except` for input validation & `FileNotFoundError` on first-time data load                       |
| **File I/O (CSV)**   | `save_to_csv()` and `load_from_csv()` using Python's built-in `csv` module                            |

---

## Class Structure

```
Transaction (base class)
├── Revenue      (overrides show())
└── Expenditure  (overrides show())

Wallet
├── transactions: list[Transaction]
├── add_transaction()
├── get_balance()
├── show_all()
├── save_to_csv()
└── load_from_csv()
```

---

## How to Run

```bash
python finance_tracker.py
```

Basic usage example:

```python
wallet = Wallet("Chrl")

wallet.add_transaction(Revenue("Monthly Salary", 5000000))
wallet.add_transaction(Expenditure("Buy Coffee", 25000))

wallet.show_all()
wallet.save_to_csv("transactions.csv")

# Program restarted → data is still there
new_wallet = Wallet("Chrl")
new_wallet.load_from_csv("transactions.csv")
new_wallet.show_all()
```
