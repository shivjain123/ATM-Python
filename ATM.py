class ATM(object):
    def __init__(self, accNo, balance=0):
        self.accNo = accNo
        self.balance = balance
        accNo = int(input("Please enter your Account Number."))
        #balance = 0

    def deposit(self, amount, balance):
        if(amount > 0):
            balance = balance + amount
            print("Your Deposit of " + amount + " was successful")
        else:
            print("Your Deposit of " + amount + " was unsuccessful; Deposit amount should be greater than 0")

    def withdrawl(self, amount, balance):
        if(amount > 0):
            if((balance - amount < 0)):
                print("You have insufficient funds for this withdrawl")
            else:
                balance = balance - amount
                print("Please take your cash from the dispenser")
        else:
            print("Withdrawl amount should be greater than 0")

    def getBalance(self, balance):
        print("The Balance in your account is " + balance)

    def getAccount(self, accNo):
        print("Your Account No. is " + accNo)

banking = ATM(12345)

print()
banking.withdrawl(60)
print()
print(banking.deposit(100))
print()
banking.withdrawl(20)
print()
banking.getBalance()
print()
banking.getAccount()
print()
