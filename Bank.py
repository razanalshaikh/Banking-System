from Database import Database
from Customer import Customer
import datetime
class Bank:
    def __init__(self):
        self.database = Database("bank.csv")
        self.customers = self.database.read_customers_from_file()


    '''
    I created this method to add new customers to the list, generated an id for customer, check inputs, and write to file
    '''
    def add_new_customer(self,first, last, password,phone, account_selection)-> bool:
        try: 
            # if user write a number in a name an error msg apear
            if not first.isalpha() or not last.isalpha():
                print("first and last names should conatin only alphabetic characters! ")
                return False
            # if user entered password length less than 8 then an error msg apear
            if len(password) < 8:
                print("password length should be at least 8")
                return False
            if not phone.isdigit():
                print("phone number must contain only digit! ")
                return False
            if len(phone) != 10:
                print("Please make sure phone number lenght is 10")
                return False
            account_Id = 10000 + len(self.customers)  
            if account_selection.lower() == "checking":
                customer = Customer(account_id=account_Id ,first_name=first,last_name=last, password=password, phone_number=phone,balance_checking=0.0)
            elif account_selection.lower() == "savings":
                customer = Customer(account_id=account_Id ,first_name=first,last_name=last, password=password, phone_number=phone,balance_savings=0.0)
            elif account_selection.lower() == "both":
                customer = Customer(account_id=account_Id ,first_name=first,last_name=last, password=password, phone_number=phone,balance_checking=0.0,balance_savings=0.0)
            else:
                print("please spcifiy account type open")

            if self.database.write_customer_to_file(customer):
                self.customers.append(customer)
                print("Customer Added Successfully.")
                return True
            else:
                print("Something wrong happend! Customer not stored in database")
                return False


        except Exception as e:
            print("Please make sure you entered correct data ")
            print(f"Error: {e}")
            return False

        
    '''
    I created this method to check if customer already regiested by phone number, because phone number a unique value, we won't have two customer with same number
    '''
    def check_customer_exsist(self, phone_number):
        try: 
            if not phone_number.isdigit():
                    print("phone number must contain only digit! ")
                    return False
            elif len(phone_number) != 10:
                    print("Please make sure phone number lenght is 10")
                    return False
            else:
                for customer in self.customers:
                    if customer.phone_number == phone_number:
                        return True
                    else:
                        print(f"Customer with phone number: {phone_number} is already registed")
                        return False
        except Exception as e :
            print(f"Error: {e}")

    '''
    login method, the customer login to system using account id and password
    before making any operations
    '''
    def login(self, account_id, password)-> Customer:
        try:
            if not account_id.isdigit():
                print("username is only numbers!")
            if len(password) < 8:
                print("password length should be at least 8")
            for customer in self.customers:
                if customer.account_id == account_id and customer.password == password:
                        return customer  
            # login failed
            print("login failed! username or password is incorrect ")
            return None
        except Exception as e:
            print(f"Error Occured: {e}")

    '''
    method to get customer by account id, so I can use it inside operation methods
    '''
    # method to get customer by id 
    def get_customer_by_id(self,account_id) -> Customer:
        for customer in self.customers:
            if customer.account_id == account_id:
                return customer
        
        return None

    '''
        reactivate method needed when account is inactive due to overdarft charges
    '''
    def reactivate_account(self,account_id):
        try:
            customer =self.get_customer_by_id(account_id)
            if customer.account_status ==  "inactive" and customer.overdarft_Count < 2:
                customer.reactivate_account()
                customer.rest_overdraft_count()
                print(f"Account {account_id} has been reactivated")
                return True
            
            return False
        
        except Exception as e:
            print(f"Error: {e}")
    

    '''
    deposit method 

    '''
    
    def deposit(self,account_id,amount,account_type)->bool:
        try:
            transaction_msg = []
            amount = float(amount)
            customer = self.get_customer_by_id(account_id=account_id)
            
            # if deposit more than amount then reactivate the account and make the deposit
            if customer.account_status == 'inactive'  and account_type == "checking" and customer.overdarft_Count >= 2 and amount > customer.balance_checking:
                self.reactivate_account(customer.account_id)
                customer.reactivate_account()
                print("Your account reactivated")
                
        
            if account_type == "checking" and customer.balance_checking is not None:
                customer_balance = float(customer.balance_checking)
                customer.balance_checking = customer_balance + amount
                self.database.updated_customer(self.customers)
                t = datetime.datetime.now().strftime("%c")
                transaction_msg = [t,"transction: Account", account_id ,"Deposited",amount,"into checking account","account current Balance: ", customer.balance_checking]
                self.database.store_transaction(transaction_msg=transaction_msg)
                print(f"Deposited {amount} into checking account")
                print(f"Your current Balance: {customer.balance_checking}")
                
                return True 

                
            elif account_type == "savings" and customer.balance_savings is not None:
                customer_balance = float(customer.balance_savings)
                customer.balance_savings = customer_balance + amount
                self.database.updated_customer(self.customers)
                t = datetime.datetime.now().strftime("%c")
                transaction_msg = [t,"transction: Account", account_id ,"Deposited",amount,"into checking account","account current Balance: ", customer.balance_savings]
                self.database.store_transaction(transaction_msg=transaction_msg)
                print(f"Deposited {amount} into savings account")
                print(f"Your current Balance: {customer.balance_savings}")
                return True 
        except Exception as e:
            print(f"Erorr: {e}")


    '''
    withdraw method
    '''   
    def withdraw(self,account_id,amount,account_type) -> bool: 
        amount = float(amount)
        customer = self.get_customer_by_id(account_id=account_id)
        
        if not customer or customer.account_status == "inactive":
            print("Account is inactive, you need to pay the overdarft fee ! ")
            return False
        
        if customer.overdarft_Count >= 2:
            print("Account is decativated, due to overdarfts, Please pay the overdraft charges to reactivate your account")
            return False
        
        if account_type == "checking":
            balance = float(customer.balance_checking)
            # overdarft idea
            if  balance == 0 or balance < 0:
                customer.overdraft_charge("checking")
                customer.increment_overdraft_count()
                overdarft_amount = float(customer.overdarft_amount)
                overdarft_amount +=35
                balance = balance - overdarft_amount
                print(balance)
                print("Your account went negative. Overdraft fee of 35 SR charged")
                
                if customer.overdarft_Count >= 2:
                    customer.deactivate_account()
                    print("Account is decativated, after 2 overdrafts")
                
            if  balance - amount < -100:
                print("cannot withdraw more than 100SR, the account is negative.")
                return False
            if balance < 0 and amount > 100:
                print("connat withdraw more than 100SR when account is negative")
                return False
            
            # make the changes
            customer.balance_checking  = balance - amount
            print(f"Withdrawn {amount} from your checking account")
            print(f"Your current Balance: {customer.balance_checking}")
            t = datetime.datetime.now().strftime("%c")
            transaction_msg = [t,"transction: Account", account_id ,"withdrawn",amount,"from your checking account","account current Balance: ", customer.balance_checking]
            self.database.store_transaction(transaction_msg=transaction_msg)

        elif account_type == "savings":
            balance_s = float(customer.balance_savings)
            if  balance_s < amount:
                print("Insuffiecient balance in your savings account")
                return False
            if balance_s < 0 : 
                print("savings account balance: 0.0")
                return False
            customer.balance_savings  = balance_s - amount
            print(f"Withdrawn {amount} from your savings account")
            print(f"Your current Balance: {customer.balance_savings}")
            t = datetime.datetime.now().strftime("%c")
            transaction_msg = [t,"transction: Account", account_id ,"withdrawn",amount,"from your savings account","account current Balance: ", customer.balance_savings]
            self.database.store_transaction(transaction_msg=transaction_msg)


        else: 
            print("something went wrong!")
        
        self.database.updated_customer(self.customers)
        return True
    '''
    check if account exisit method, this method will checks if account exisit for sepcefic customer
    '''
    def check_account_exsist(self,account_id,account_type):
        try:  
            customer = self.get_customer_by_id(account_id=account_id)
            if account_type.lower() == "checking":
                checking = customer.balance_checking
                if checking is None or checking == "":
                    print("You don't have a checking Account")
                    return False
                else:
                    return True         

            if account_type.lower() == "savings": 
                savings = customer.balance_savings
                if savings is None or savings == "":
                    print("You don't have a savings account") 
                    return False
                else: 
                    return True
            
        except Exception as e: 
            print(f" Erorr: {e}")
            return False


    '''
    transfer between personal account 
    '''

    def transfer_between_personal_account(self,account_id, from_account_Type,to_account_type,amount):
        try:  
            customer = self.get_customer_by_id(account_id=account_id)
            amount = float(amount)
            transaction_msg =[]
            # if account status is inactive, no transactions allowed
            if not customer or customer.account_status == "inactive":
                print("Account is inactive")
                return False
            # before making operation I will if customer have two accounts, if customer dosen't have an account then it will be initialize
            print(customer.balance_checking)
            print(customer.balance_savings)
            account_ch=self.check_account_exsist(customer.account_id,account_type="checking")
            account_sv=self.check_account_exsist(customer.account_id,account_type="savings")
            print(customer.balance_savings)
            print(customer.balance_checking)
                
            if account_ch is False:
                ch_balance = 0.0
                customer.balance_checking = ch_balance
                print("checking account Created")
            if account_sv is False:
                sv_balance = 0.0
                customer.balance_savings = sv_balance
                print("savings account Created")

            # transfer 
            if from_account_Type == "checking" and to_account_type =="savings":
                print (f"result: {customer.balance_checking}")
                ch_balance = float(customer.balance_checking)
                if  ch_balance < amount :
                    print("Insuffiecient balance in your checikng account")
                    return False
                customer.balance_checking = float(customer.balance_checking) - amount
                customer.balance_savings = float(customer.balance_savings) + amount
                t = datetime.datetime.now().strftime("%c")
                transaction_msg = [t,"transction: Account", account_id ,"Transferred",amount,"from checking account to savings"," checking current balance: ",customer.balance_checking, " current savings balance: ",customer.balance_savings]
                self.database.store_transaction(transaction_msg=transaction_msg)
                print(f"Transferred {amount} from checking to savings account.")

            if from_account_Type == "savings" and to_account_type == "checking":
                sv_balance = float(customer.balance_savings)
                if  sv_balance < amount :
                    print("Insuffiecient balance in your savings account")
                    return False
            
                customer.balance_savings = float(customer.balance_savings) - amount
                customer.balance_checking = float(customer.balance_checking) + amount
                t = datetime.datetime.now().strftime("%c")
                transaction_msg = [t,"transction: Account", account_id ,"Transferred",amount,"from savings account to checking "," checking current balance: ",customer.balance_checking, " current savings balance: ",customer.balance_savings]
                self.database.store_transaction(transaction_msg=transaction_msg)
                print(f"Transferred {amount} from savings to checking account.")

            self.database.updated_customer(self.customers)
            return True
            
        except Exception as e: 
            print(f" Erorr: {e}")
            return False  

    '''
    Transfer to another customer account
    I assume that the transfer will be to the checking account of the other customer 
    but customer can deceide from which account the transfering will be either from a checking or savings
    needed argument to complete this transaction: logged_in_customer_account_id from_account_type to__account_id amount
    '''
    def transfer_to_another_customer(self,from_account_type,sender_account_id,recipient_account_id,amount):
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount can't be zero or minus value")
            sender = self.get_customer_by_id(sender_account_id)
            recipient = self.get_customer_by_id(recipient_account_id)
            if recipient is None:
                print("make sure to enter a correct recipient id! ")
                return False
            if not sender or sender.account_status == "inactive":
                print("Account is inactive")
                return False
            # here to check if the recpient have a checking account
            recipient_account_exisit = self.check_account_exsist(recipient_account_id,"checking")
            if recipient_account_exisit is False:
                recipient_balance = 0.0
                recipient.balance_checking = recipient_balance

            # convert type of checking balance to float to use it again
            recipient_balance = float(recipient.balance_checking)

            # depening on the type will 
            if from_account_type.lower() == "checking":
            # first check if account exisit
                    sender_account_exisit = self.check_account_exsist(sender_account_id,"checking")
                    if sender_account_exisit is False:
                        print("New checking account created")
                        print("Your account Balance is zero you can't make a transfer! ")
                        sender_checking = 0.0 
                        sender.balance_checking = sender_checking
                    # check balance if zero can't make a transfer
                    if sender.balance_checking == "0.0":
                        print("Your account Balance is zero you can't make a transfer! ")  
                        return False  
                    # convert type of checking balance to float to use it again
                    checking_balance_sender = float(sender.balance_checking)
                    if  checking_balance_sender< amount:
                        print("Insuffiecient balance in your checking account")
                        return False

                    sender.balance_checking = checking_balance_sender - amount
                    recipient.balance_checking = recipient_balance + amount
                    t = datetime.datetime.now().strftime("%c")
                    transaction_msg = [t,"transction: Account", sender_account_id ,"Transferred from your checking account: ",amount,"to Account: ", recipient.account_id, " and your curent account balance: ",sender.balance_checking]
                    print(f"Transferred {amount} from your checking account to recipient checking account.")
                    self.database.updated_customer(self.customers)
                    self.database.store_transaction(transaction_msg=transaction_msg)
                    return True

            elif from_account_type.lower() == "savings":        
                # first check if account exisit
                    sender_account_exisit = self.check_account_exsist(sender_account_id,"savings")
                    if sender_account_exisit is False:
                        print("New savings account created")
                        print("Your account Balance is zero you can't make a transfer! ")
                        sender_savings= 0.0 
                        sender.balance_savings = sender_savings
                    # check balance if zero can't make a transfer
                    if sender.balance_savings == "0.0":
                        print("Your account Balance is zero you can't make a transfer! ")  
                        return False  
                    # convert type of savings balance to float to use it again
                    savings_balance_sender = float(sender.balance_savings)
                    if  savings_balance_sender < amount:
                        print("Insuffiecient balance in your checking account")
                        return False
                    
                    sender.balance_savings = savings_balance_sender - amount
                    recipient.balance_checking = recipient_balance + amount
                    t = datetime.datetime.now().strftime("%c")
                    transaction_msg = [t,"transction: Account", sender_account_id ,"Transferred from your savings account: ",amount,"to Account: ", recipient.account_id, " and your current balance : ", sender.balance_savings]
                    print(f"Transferred {amount} from your savings account to recipient checking account.")
                    self.database.updated_customer(self.customers)
                    self.database.store_transaction(transaction_msg=transaction_msg)
                    return True
            else:
                print("You should either checking or savings account to transfer from! ")
        except Exception as e:
            print(f"Erorr: {e}")

        