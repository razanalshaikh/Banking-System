
import csv
from Customer import Customer

# I created a class as database, because we will only have one database which is the file.
class Database():

    def __init__(self, file_name):
        self.file_name = file_name

    """
    In database class, we have two methods, method read customers from the file, and a method that add new customer to the file
    """
    def read_customers_from_file(self)-> list:
        try:
            # list of customer to store customers info after reading from file
            customers= []
            with open(self.file_name,mode='r') as file:
                csv_file = csv.reader(file,delimiter=";")
                # read each row and add it to the list
                for row in csv_file:
                    # if row to check that there's a data in row
                    if row:
                        customer = Customer(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                        customers.append(customer)
                        
        # this exception is exisit in python exception library, if file not found we will get file not found error msg
        except FileNotFoundError:
                print("File not found")
        else:
            # if no error raised then data is read from file successfully
            return customers

    '''
        Write Customer to file
        inside this method we add the new customer information to the file 
        I used the a mode to append to file instead of w mode 
        because w mode will rewrite on the file and delete the stored data for another customers
    # '''
    def write_customer_to_file(self, customer)-> bool: 
        try:
            with open(self.file_name,mode="a",newline='') as file:
                    csv_writer= csv.writer(file,delimiter=";")
                    # we need to convert the obj to a list,
                    # so we can store the new customer information to the file
                    customer_info = [customer.account_id, customer.first_name, customer.last_name, 
                                    customer.password, customer.phone_number,customer.balance_checking, customer.balance_savings,customer.account_status]
                    csv_writer.writerow(customer_info)
                    print(f"{customer.first_name} {customer.last_name} information added to database sucssfully")
                    return True
        except FileNotFoundError:
                print("File not found")
                return False
        except Exception as e:
                print(f"Error Occured: {e}")

    def updated_customer(self, customers): 
        try:
            with open("bank.csv","w",newline='') as file:
                    csv_writer= csv.writer(file,delimiter=";")
                    for customer in customers:
                        # the list is a list of customers, this is mean that we need to convert the obj to list 
                        # to insert each row in list as a row in flie 
                        customer_info = [customer.account_id, customer.first_name, customer.last_name, 
                                        customer.password,customer.phone_number, customer.balance_checking, customer.balance_savings,customer.account_status]
                        csv_writer.writerow(customer_info)
        except FileNotFoundError:
                
                print("File not found")
    '''
    transction history
    this method to store alll transaction happend when code is running 
    '''

    def store_transaction(self, transaction_msg):
        try:
            with open("transaction.csv",mode="a",newline='') as file:
                csv_writer= csv.writer(file,delimiter=':')
                csv_writer.writerow(transaction_msg)

        except FileNotFoundError:
                print("File not found")