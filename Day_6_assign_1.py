class bankAccount():
    def __init__(self,OwnerName,Balance):
        self.OwnerName = OwnerName
        self.Balance = Balance
    def getDetails(self):
        print("name:",self.OwnerName)
        print("balance is:",self.Balance)
        print("   ")
    def deposit(self,a):
        if a>0:
            self.b = self.Balance+a
        else:
            print("innsufficient")
            
    def getDetailsad(self):
        print("name:",self.OwnerName)
        print("balance is:",self.b)
        print("   ")
    
    def withdraw(self):
        continueTransaction = "y"
        
        while continueTransaction.lower() != "n":
            amt = int(input("enter:"))
            if amt <= self.b:
                self.f = self.b-amt
                print("Collect your cash")
            else:
                print("Insufficent amount entered")
                print(" ")
            continueTransaction = input("Do you want to continue transaction y/n")
    def getDetailsaw(self):
        print("name:",self.OwnerName)
        print("balance is:",self.f)
        print("   ")
    
x = bankAccount("raj",0)
x.getDetails()
x.deposit(1000)
x.getDetailsad()
x.withdraw()
x.getDetailsaw()





