class account:
    def __init__(self):
        self.bal=0
        print("account created")
    def deposit(self):
        amo=int(input())
        self.bal+=amo
        print("deposited amount",amo)
    def withdraw(self):

        amo=int(input("enter the with"))
        if self.bal>=amo:
            self.bal-=amo
            print("withdraw successfully",amo)
        else:
            print("sufficient amoutnot there in")
    def dis(self):
        print("total balance:",self.bal)
h=account()
h.deposit()
h.withdraw()
h.dis()







