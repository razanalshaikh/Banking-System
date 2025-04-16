# Banking-Project

### Project Description  
A console-based banking system in Python that simulates real-world operations using a CSV file as database. Features include secure login, account creation, deposits, withdrawals, fund transfers, and overdraft protection with automated fees and account status management. Built using object-oriented principles, file and exception handling, and a test-driven development approach, with transaction history tracking and timestamped records.

---

### Project Content

There are 4 classes in this project:

#### Main Class  
Inside this class, we have the main menu. The program takes user input, initializes the bank object, validates user inputs, and calls the required functions.

---

#### Bank Class  
Manages all operations of the program. It creates a list of customers using a database object.

**Functions:**
- `add_new_customer`
- `check_customer_exist` (by phone number)
- `check_account_exist`
- `login`
- `get_customer_by_id`
- `reactivate_account`
- `deposit`
- `withdraw`
- `transfer_between_personal_account`
- `transfer_to_another_customer`

---

#### Customer Class  
An entity class that represents each customer with a unique account ID and other related attributes.

---

#### Database Class  
Handles reading and writing to the CSV database.

**Functions:**
- `read_customers_from_file`
- `write_customer_to_file`
- `update_customer`
- `store_transaction`

---

#### TDD Class (Test-Driven Development)  
This class includes unit tests for all functions to ensure code reliability.


---
#### There are two files in this project:
### **bank.csv:** 
Store customers information
### **transaction.csv:** 
Store all customers transactions.
