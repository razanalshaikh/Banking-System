import unittest
import csv
from Database import Database
from Customer import Customer
from Bank import Bank

class TestFunctions(unittest.TestCase):
    
    def test_read_file(self):
        # we need a db object
        db = Database("bank.csv")
        result = db.read_customers_from_file()
        self.assertIsInstance(result, list)
        # to check if there's registerd customer and file not empty
        self.assertGreater(len(result),0)
        
    def test_write_to_file(self):
        db = Database("bank.csv")
        customer = Customer("Sara","Alshaikh","password01","0500535457",40000,3300)
        result = db.write_customer_to_file(customer)
        self.assertTrue(result)

    def test_add_new_customer(self):
        bank = Bank()
        result = bank.add_new_customer("aziz","Alshaikh","password01","0500535456","savings")
        self.assertTrue(result)
        result = bank.add_new_customer("Raghad","Alshaikh","password01","05005444456"," ")
        self.assertFalse(result)

    def test_check_customer_exists(self):
        bank = Bank()
        result = bank.check_customer_exsist("0555555555")
        self.assertFalse(result)
        result = bank.check_customer_exsist("05jfjfj")
        self.assertFalse(result)
        result = bank.check_customer_exsist("0500000000000")
    
    def test_login(self):
            bank = Bank()
            result = bank.login("10000","password02")
            self.assertIsInstance(result, Customer)
            self.assertIsNone(bank.login("10006","passsword11"))

    def test_deposit(self):
            bank = Bank()
            # deposit to checking account
            result = bank.deposit("10002",100,"checking")
            self.assertTrue(result)
    
    def test_withdrawn(self):
            bank = Bank()
            # withdraw from checking account
            result = bank.withdraw("10002",100,"checking")
            self.assertTrue(result)
            # withdraw from account 0
            result = bank.withdraw("10006",10,"checking")
            self.assertTrue(result)
            # try again will deactivte
            result = bank.withdraw("10006",10,"checking")
            self.assertTrue(result)
            # try again will show error msg that you account inactive
            

    def test_check_account_exisit(self):
        b = Bank()
        # check a customer with a checking account
        self.assertTrue(b.check_account_exsist("10000","checking"))
        # check a customer with no checking account
        self.assertFalse(b.check_account_exsist("10003","checking"))
        # check a customer with a checking account
        self.assertTrue(b.check_account_exsist("10000","savings"))
        # check a customer with no checking account
        self.assertFalse(b.check_account_exsist("10003","savings"))

        # check type
        self.assertIsInstance(b.check_account_exsist("10003","checking"),bool)
        
    # Test for two types of transfer
            # Test transfer btw personal account
    def test_transfer_between_personal_account(self):
        bank = Bank()
        # 10002 transfer from checking to savings, where savings is None or = " "
        self.assertTrue(bank.transfer_between_personal_account("10002","checking","savings", 1000))
            
            # Test transfer to another customer

    def test_transfer_to_another_Customer(self):
        b = Bank()
        # transfer from checking to checking 
        self.assertTrue(b.transfer_to_another_customer(from_account_type="checking",sender_account_id="10000",recipient_account_id="10004",amount=255))
        # transfer from checking to checking but wrong id for recipent
        self.assertFalse(b.transfer_to_another_customer(from_account_type="checking",sender_account_id="10000",recipient_account_id="1004",amount=255))
        # if entered as amount 0 or leess than zzero in transfering values
        self.assertTrue(b.transfer_to_another_customer(from_account_type="checking",sender_account_id="10000",recipient_account_id="10004",amount=0))
        # return type for this method always Boolean
        self.assertIsInstance(b.transfer_to_another_customer(from_account_type="checking",sender_account_id="10000",recipient_account_id="10004",amount=0),bool)



if __name__ == "__main__":
    # improve the information included in the output
    # with this just need to run the file. pyhton main_test()
    unittest.main(verbosity=2)