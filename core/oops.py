''' the basic syntax for oops is 
    class classname:
        properties
        methods/functionalities
    obj = classname(values)
init - constructor - to initialize the object
self - current object(holds the address of current object) same as cls - class itself
instance method - to access instance level properties
@classmethod - to access class level properties
@staticmethod - to create a utility function

'''


#1
class meta:
    ceo = 'mark'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = meta('2 trillion')
obj.disp()
meta.disp()
meta.ch(meta,'narendra modi')
meta.add(2,4)
#2
class alphabet:
    ceo = 'sundar'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = alphabet('3 trillion')
obj.disp()
obj.xyz()
alphabet.disp()
alphabet.ch(alphabet,'narendra modi')
alphabet.add(2,4)
#3
class oracle:
    ceo = 'bsfgfd'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = oracle('3 trillion')
obj.disp()
obj.xyz()
oracle.disp()
oracle.ch(oracle,'narendra modi')
oracle.add(2,4)
#4
class tiktok:
    ceo = 'chinese'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = tiktok('1 trillion')
obj.disp()
obj.xyz()
tiktok.disp()
tiktok.ch(tiktok,'yogi adityanath')
tiktok.add(2,5)
#5
class chatgpt:
    ceo = 'sam altman'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = chatgpt('1 trillion')
obj.disp()
obj.xyz()
chatgpt.disp()
chatgpt.ch(chatgpt,'yogi adityanath')
chatgpt.add(2,5)
#6
class amazon:
    ceo = 'jeff bezos'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = amazon('1 trillion')
obj.disp()
obj.xyz()
amazon.disp()
amazon.ch(amazon,'hemanta biswa sharma')
amazon.add(2,7)
#7
class instagram:
    ceo = 'mark zuckerberg'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = instagram('3 trillion')
obj.disp()
obj.xyz()
instagram.disp()
instagram.ch(instagram,'hemanta biswa sharma')
instagram.add(2,7)
#8
class nvidia:
    ceo = 'chiang'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = nvidia('4 trillion')
obj.disp()
obj.xyz()
nvidia.disp()
nvidia.ch(nvidia,'mukesh ambani')
nvidia.add(2,7)
#9
class Tata:
    ceo = 'Sir Ratan Tata'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = Tata('500 Billion')
obj.disp()
obj.xyz()
Tata.disp()
Tata.ch(Tata,'mukesh ambani')
Tata.add(2,7)
#10
class infotact:
    ceo = 'habibi'
    def __init__(self,val):
        self.val = val
    def disp(self):
        print(f'valuation is {self.val}')
    def xyz(self):
        print("it's an object")
    @classmethod
    def disp(cls):
        print(f"ceo is {cls.ceo}")
    def ch(cls,new):
        cls.ceo = new
        print(f'new ceo is {cls.ceo}')
    @staticmethod
    def add(x,y):
        print(x + y)
obj = infotact('10 Rs')
obj.disp()
obj.xyz()
infotact.disp()
infotact.ch(infotact,'come to dubai')
infotact.add(2,7)
#wap to get the first and last occurance of an element
class solution:
    def k(self,nums,tar):
        if tar not in nums:
            return [-1,-1]
        i = nums.index(tar)
        j = 0
        while i < len(nums):
            if nums[i] == tar:
                j = i
            i += 1
        return [nums.index(tar),j]
print(solution.k(solution,eval(input("enter a list: ")),int(input("enter a number: "))))