class BankAccount:
   def __init__(self,account_number,account_holder_name,initial_balance=0.0):
     self.__account_number = account_number
     self.__account_holder_name=    account_holder_name
     self.__account_balance = initial_balance
   def deposit (self, amount):
      if amount > 0:
         self.__account_balance += amount
         print("Deposited ₹{}. New balance:₹{}".format (amount,self.__account_balance))
      else: 
          print ("Invalid deposit anount.Please deposit a positive amount.")

   def Withdraw(self,amount):
        if amount > 0 and amount <= self.__account_balance:
          self.__account_balance_= amount
          print("Withdraw ₹{}. New balance:₹{}".format(amount,self.__account_balance))
        else:
          print("Invalid withdraw amount or insufficient balance.")

   def display_balance(self):
      print ("Account balance for{} (Account #{}):₹ {}".format(
        self.__account_holder_name,self.__account_number,
        self.__account_balance))
                                                               

account=BankAccount(account_number="12345678",account_holder_name="Sheela",initial_balance=5000.0)
 

account.display_balance()
account.deposit(500.0)
account.Withdraw(200.0)
account.Withdraw(2000.0)
account.display_balance()