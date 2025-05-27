from RBIApp import RBI



class hdfc(RBI):
    InitialBalance = 100
    amt =int(input('Enter a value '))
    def giveLoans(self):
        print('give loans')
    def withdrawAmount(self):
        print(f"Amount to be withdrawn {self.amt}")
    def checkBalance(self):
        self.a=self.InitialBalance-self.amt
        print(f'Amount Left {self.a}')
    def depositAmount(self):
        print('amount deposited')
   # def 
   
    

hdfc=hdfc()
hdfc.withdrawAmount()
hdfc.checkBalance()

