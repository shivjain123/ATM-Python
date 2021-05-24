class ATM(object):
    def __init__(self):
        self.accNo = int(input("Please enter your Account Number."))
        self.balance = 100000
        self.amount = int(input("Please enter the Amount you want to deposit/withdraw."))

    def deposit(self):
        if(self.amount > 0):
            self.balance = self.balance + self.amount
            print("Your Deposit of " + str(self.amount) + " was successful")
        else:
            print("Your Deposit of " + str(self.amount) +
                  " was unsuccessful; Deposit amount should be greater than 0")

    def withdrawl(self):
        if(self.amount > 0):
            if((self.balance - self.amount < 0)):
                print("You have insufficient funds for this withdrawl")
            else:
                self.balance = self.balance - self.amount
                print("Please take your cash from the dispenser")
        else:
            print("Withdrawl amount should be greater than 0")

    def getBalance(self):
        print("The Balance in your account is " + str(self.balance))

    def getAccount(self):
        accNo = self.accNo
        print("Your Account No. is " + str(accNo))

banking = ATM()

print()
banking.withdrawl()
print()
banking.getBalance()
print()
banking.deposit()
print()
banking.getBalance()
print()
banking.getAccount()
print()
