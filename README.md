# Banking-Project
### There are 4 classes in this project: 
##### **main class:**
Inside this class we have the main menu, and inside the main menu we take user input, Initialize the bank object, vaildate the inputs from user, and then call the rquired function. 
---
##### **Bank class:** 
Inside the bank class, the customers list is created using a database object, in this class we have all required operations for the program.
Functions list:
- add_new_customer.
- check_customer_exsist, using phone number.
- check_account_exsist
- login function.
- Get_customer_by_id.
- reactivate_account: when the overdaft is paid.
- deposit
- withdraw
- transfer_between_personal_account
- transfer_to_another_customer

---
##### **Customer class:** 
An entity class that represents customers in a system. each csutomer has a unigue identifier which is account id, and have another attributes. 

---
##### **Database class:** 
This class is to read and write to database, which CSV file. 
Functions list:
- read_customers_from_file: this method used to read all customers from file and store it into a list of customers, so we can use it in the program.
- write_customer_to_file: this method used to append a new customer to the database when a new customer is added.
- updated_customer: this method update all customers information on the databse when any transaction happen or any changes happen to customers info.
- store_transaction: this method is used to write all tranactions happend when customers make any operation, when they are logged in.  
---
##### **TDD class(test-driven development (TDD) approach):** 
In this class, I tested all functions using unit test. 

---
#### There are two files in this project:
### **bank.csv:** 
Store customers information
### **transaction.csv:** 
Store all customers transactions.
