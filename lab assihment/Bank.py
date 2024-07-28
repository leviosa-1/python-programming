class BankAccount:
    
    def __init__(self,Account_num,Bal=0.0):
        self.Account_num=Account_num
        self.Bal=Bal
        
    def get_bal(self):
        print("Balance :",self.Bal)
        
    def get_acc_num(self):
        print("Account NUmber :",self.Account_num)
    
    def deposite(self,ammount):
        if ammount>0:
            self.Bal+=ammount
            print(f"deposited Ammount : {ammount} \n Current Balance : {self.Bal}" )
        else :
            print("invalid Deposite Ammount")
            
    def withdraw(self,ammount):
        if 0 < ammount <=self.Bal :
            self.Bal-=ammount
            print(f"Withdraw Ammount : {ammount} \n current ammount : {self.Bal}")
        else :
            print("Insufficient funds")
account=BankAccount(99511051004266,1000)
account.get_acc_num()
account.get_bal()
account.deposite(5289.56)
account.withdraw(2896.56)