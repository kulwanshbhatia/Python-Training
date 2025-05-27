from RBIApp import RBI

class SBI(RBI):
        def giveLoans(self):
            print('SBI Provides Loan')
        def withdrawAmount(self):
            print('sbi withdraw')
        def depositAmount(self):
            print('in sbi amount deposited')
        def checkBalance(self):
             print('Check Balance')

sbi=SBI()
sbi.giveLoans()
sbi.checkBalance()
sbi.depositAmount()
