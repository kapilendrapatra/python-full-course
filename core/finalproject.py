#this is a project for core python course
class Mybank:
    ifsc = 'mb02624'
    def __init__(self,name,mob,ac,dep):
        self.name = name
        self.mob = mob
        self.ac = ac
        self.dep = dep
    def credit(self,amt):
        self.dep = self.dep + amt
    def debit(self,amt):
        if amt > self.dep:
            print("Insuficient Balance")
            print(f'Your balance is {self.dep}')
        self.dep -= amt
c2 = Mybank('Mayank','9836738237','174837539584738',int(input("enter first deposite: ")))
while True:
    dc = input('credit or debit or check or done : ').lower()
    if dc == 'credit':
        c2.credit(int(input("Enter the amount: ")))
    elif dc == 'debit':
        c2.debit(int(input("Enter the amount: ")))
    elif dc == 'check':
        print(f"total bank balance is {c2.dep}")
    elif dc == 'done':
        break
    else:
        print("wrong input")

#THANK YOU FOR USING THIS COURSE.
