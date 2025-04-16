
import csv, Customer, Database, Bank
from Customer import Customer
from Database import Database
from Bank import Bank

if __name__ == "__main__":
    bank = Bank()
    while(True):
        try: 
            print("######################################################")
            print("################ Welcome to ACME Bank ################")
            print("######################################################")
            print("Enter (1) to add new customer \nEnter (2) to make a withdrwal, deposit, transfer \nEnter (3) exit :")
            choice = input()
            if choice == "1":
                print("################ Add New Customer ################")
                first = input("Enter your first name: ")
                last = input("Enter your last name: ")
                password = input("Enter a password: ")
                phone = input("Enter your Phone Number: ")
                # to specify what
                account_selection =input("Enter (checking) if you want to have a checking account only\nEnter (savings) if you want to have a savings account only \nEnter (both) if you want to have a checking account and savings account: ")
                if account_selection.lower() == "checking" or  account_selection.lower() == "savings" or  account_selection.lower() == "both":
                    check_customer = bank.check_customer_exsist(phone)
                    # if customer exisit then add it 
                    if  not check_customer:
                        # not exisit add this
                        bank.add_new_customer(first=first,last=last,password=password,phone=phone,account_selection=account_selection)
                else:    
                    print("please selcet correct account type, try again!")                   
            elif choice =="2":
                print("################ Login ################")
                account_id = input("Username (Account ID): ")
                password = input("Password: ")
                # here login flow
                logged_in_customer = bank.login(account_id=account_id,password=password)
                if logged_in_customer is None:
                    print("please try to login again!")
                else:
                    while(True):
                        print(f"################ Welcome {logged_in_customer.first_name} {logged_in_customer.last_name } ################")
                        print(f"Your account status is: {logged_in_customer.account_status}")
                        account_type = input("Choose an account (checking / savings): ")
                        if account_type == "checking":
                            if logged_in_customer.balance_checking is None or logged_in_customer.balance_checking == "": 
                                print("you don't have a checking account")
                                open_checking = input("Do you want to open a checking acccount (YES/NO)? ")
                                if open_checking.upper() == "YES":
                                        logged_in_customer.balance_checking = 0.0
                                        print("New checking account created :)! ")
                                        bank.update_customers_info()
                                elif open_checking.upper() == "NO":
                                        print("OK! you don't have a checking account.")
                                else:
                                        print("invaild input! ")
                            else:
                                print("################ choose an operation ################")
                                choice = input("Enter (1) Deposit \nEnter (2) Withdraw  \nEnter (3) Transfer :")
                                if choice == "1":
                                    # call Deposit function
                                    amount = input("amount: ")
                                    bank.deposit(account_id=logged_in_customer.account_id,account_type=account_type,amount=amount)
                                elif choice == "2":
                                    # call Withdraw function
                                    amount = input("amount: ")
                                    bank.withdraw(account_id=logged_in_customer.account_id,account_type=account_type,amount=amount)
                                elif choice == "3":
                                    # call transfer function
                                    print("################ Transfer ################")
                                    choice = input("Enter (1) Transfer Between Personal Account \nEnter (2) Transfer to another customer: ")
                                    if choice == "1":
                                        # call transfer between personal account
                                        # decide from which account, to which account
                                        print("################ Transfer between personal account ################")
                                        choice = input("Enter (1) to transfer from checking to savings:\nEnter (2) to transfer from savings to checking: ")
                                        amount = input("amount: ")
                                        if choice == "1":
                                            from_account_type = "checking"
                                            to_account_type = "savings"
                                            bank.transfer_between_personal_account(from_account_Type=from_account_type,to_account_type=to_account_type,account_id=logged_in_customer.account_id,amount=amount)
                                        elif choice == "2":
                                            from_account_type = "savings"
                                            to_account_type = "checking"
                                            bank.transfer_between_personal_account(from_account_Type=from_account_type,to_account_type=to_account_type,account_id=logged_in_customer.account_id,amount=amount)

                                        else:
                                            print("invalid input! Please Try again!")
                                    elif choice == "2":
                                        # call transfer between two customers
                                        print("################ Transfer to another customer account ################")
                                        recipient_account_id = input("Enter Recipient account id: ")
                                        amount = input("Transfer amount: ")
                                        bank.transfer_to_another_customer(recipient_account_id=recipient_account_id,sender_account_id=logged_in_customer.account_id,from_account_type=account_type,amount=amount)                                    
                                    else: 
                                        print("Error! You should select either 1 or 2")
                                else: 
                                    print("Please select correct transfer opeartion!")

                        elif account_type == "savings":
                            if logged_in_customer.balance_savings is None or logged_in_customer.balance_savings == "":
                                print("you don't have a savings account")
                                open_savings = input("Do you want to open a savings acccount (YES/NO)? ")
                                if open_savings.upper() == "YES":
                                    logged_in_customer.balance_savings = 0.0
                                    print("New checking account created :)! ")
                                    bank.update_customers_info()
                                elif open_savings.upper() == "NO":
                                    print("OK! you don't have a savings account.")
                                else:
                                    print("invaild input! ")
                            else:
                                print("################ choose an operation ################")
                                choice = input("Enter (1) Deposit \nEnter (2) Withdraw  \nEnter (3) Transfer :")
                                if choice == "1":
                                    # call Deposit function
                                    amount = input("amount: ")
                                    bank.deposit(account_id=logged_in_customer.account_id,account_type=account_type,amount=amount)
                                elif choice == "2":
                                    # call Withdraw function
                                    amount = input("amount: ")
                                    bank.withdraw(account_id=logged_in_customer.account_id,account_type=account_type,amount=amount)
                                elif choice == "3":
                                    # call transfer function
                                    print("################ Transfer ################")
                                    choice = input("Enter (1) Transfer Between Personal Account \nEnter (2) Transfer to another customer: ")
                                    if choice == "1":
                                        # call transfer between personal account
                                        # decide from which account, to which account
                                        print("################ Transfer between personal account ################")
                                        choice = input("Enter (1) to transfer from checking to savings:\nEnter (2) to transfer from savings to checking: ")
                                        amount = input("amount: ")
                                        if choice == "1":
                                            from_account_type = "checking"
                                            to_account_type = "savings"
                                            bank.transfer_between_personal_account(from_account_Type=from_account_type,to_account_type=to_account_type,account_id=logged_in_customer.account_id,amount=amount)
                                        elif choice == "2":
                                            from_account_type = "savings"
                                            to_account_type = "checking"
                                            bank.transfer_between_personal_account(from_account_Type=from_account_type,to_account_type=to_account_type,account_id=logged_in_customer.account_id,amount=amount)
                                        else:
                                            print("invalid input! Please Try again!")
                                    elif choice == "2":
                                        # call transfer between two customers
                                        print("################ Transfer to another customer account ################")
                                        recipient_account_id = input("Enter Recipient account id: ")
                                        amount = input("Transfer amount: ")
                                        bank.transfer_to_another_customer(recipient_account_id=recipient_account_id,sender_account_id=logged_in_customer.account_id,from_account_type=account_type,amount=amount)                                    
                                    else: 
                                        print("Error! You should select either 1 or 2")
                                else: 
                                    print("Please select correct transfer opeartion!")
                        else: 
                            print("Error: You need to choose either checking or savings account!")
                
                        logout_control = input("Enter 3 to log out:")
                        if(logout_control == "3"):
                            print("Back to main Menu")
                            break
                        
            elif choice == "3":
                print("Bye, see you again!")
                exit()
            else:
                print("Invaild input! please try again")
        except Exception as e: 
            print(f"Error: {e}")
