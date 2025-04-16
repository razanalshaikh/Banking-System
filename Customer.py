'''
Customer class to create a customers list of customer obj
'''
class Customer():
    def __init__(self,account_id, first_name,last_name,password, phone_number, balance_checking=None, balance_savings=None, account_status = 'active'):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.phone_number = phone_number
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings
        self.account_status = account_status
        self.overdarft_Count = 0.0
        self.overdarft_fee_status = False
        self.overdarft_amount = 0.0
    
    def __str__(self):
        return f"Customer Info: Name: {self.first_name} {self.last_name}, Phone Number: {self.phone_number} ,Account Id: {self.account_id}, Account Status: {self.account_status}"
    
    
    # methods to make changes on the account status
    def deactivate_account(self):
        self.account_status = 'inactive'
    # if customer paid by make a deposit the overdarft charges then reactivate account
    def reactivate_account(self):
        self.account_status = 'active'
    
    # overdarft count
    # we need this method when overdarft occur, so we count how many times overdarft happened
    # only two allowed then account decativate
    def increment_overdraft_count(self):
        self.overdarft_Count += 1
    # if customer paid all overdraft charges then we reset the overdarft count to become 0
    def rest_overdraft_count(self):
        self.overdarft_Count = 0.0
    
    # overdraft charge method 
    def overdraft_charge(self, account_type):
        try: 
            if account_type == "checking":
                checking_balance = float(self.balance_checking)
                if checking_balance is not None and  checking_balance < 0:
                    self.balance_checking = checking_balance - 35
        except Exception as e:
            print(f"Error: {e}")
        
