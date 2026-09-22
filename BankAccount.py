class BankAcc:
    def __init__(self):
        self.balance = 0
        print(f"welcome to the ATM, your balance is {self.balance}")
    def deposit(self):
        amount = float(input("Enter your deposit:"))
        self.balance += amount
        print(f"your balance is: {self.balance}")
    def withdrawl(self):
        amount = float(input("Enter your withdrawl:"))
        if amount > self.balance:
            print("you can't withdrawl that much, try again")
        else:
            self.balance -=amount
    def display(self):
        print(f"you have {self.balance} in your account")
        

app = BankAcc() #instatiate object

exit = False

while exit == False:
    number = int(input("do you want to withdrawl (1) or depost (2)?"))

    if number == 1:
        app.withdrawl()
    elif number == 2:
        app.deposit()

    app.display()
    
    answer = input("do you wish to exist? Y/N (you must tap Y or N and then press Enter)")
    if answer == 'Y' or answer == 'y':
        break
    elif answer == 'N' or answer == 'n':
        continue
    