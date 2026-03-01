class Bankaccount:
    bank_name = "canara"

    def __init__(self,cname,acc,age,balance):
        self.cname = cname
        self.acc = acc
        self.age = age
        self.balance = balance

    def detail(self):
        print(f"CNAme:{self.cname}")
        print(f"acc:{self.acc}")
        print(f"age:{self.age}")
        print(f"balance:{self.balance}")

    def deposit(self,depo):
        self.balance += depo
        print(f"Balance after deposit {self.balance} ")


class saving_account(Bankaccount):

    def __init__(self,cname,acc,age,balance,fee):
        super().__init__(cname,acc,age,balance)
        self.fee =fee

    

    def withdraw(self,withd):
        if self.balance < withd +self.fee:
            print("insufficent balanece")
        else:
            self.balance -= withd + self.fee
            print(f"after withdraw:{self.balance}")

acc1 = Bankaccount('Sharath',123456,22,5000)

acc1.detail()
acc1.deposit(1000)

print("----------------------------------------------")

sav1 =saving_account('vk',465415,21,6000,40)

sav1.detail()
sav1.withdraw(50000)