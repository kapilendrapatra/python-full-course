#wap to display all frequency of vowels present in your name.
c = 0
for i in "aeiou":
    for j in "kapilendra patra":
        if i == j:
            c += 1
    print(i,c,sep=",")
    c = 0
#wap to reverse a string without slicing method
a = input("Enterr a string: ")
b = ''
for i in a:
    b = i + b
print(b)
#wap to prinnt all integer numbers in range 100.
for i in range(2,101,2):
    print(i)
#WAP to only extract the odd numbers from a list.
a = eval(input("enter a list: "))
b = []
for i in a:
    if str(i)[-1] in "13579":
        b += [i]
print(b)
# Q63.Write a program to get the following output(count no of vowels)
# input=’hai hello’
# output=[‘hai’:2 , ‘hello’:2]
a = input("enter a string: ").split()
b = []
for i in a:
    c = 0
    for j in i:
        if j in "aeiou":
            c += 1
    b += [f"'{i}':{c}"]
print(b)
#WAP to print repeated values
a = eval(input("enter "))
b = []
c = []
d = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
for i in b:
    if i not in c:
        d.append(i)
print(d)
#WAP to get the output
a = eval(input("enter a tuple: "))
b = {}
for i in a:
    if type(i) == str:
        b[i] = len(i)
print(b)
#WAP to print the occurance
a = input("enter a string: ")
b = ""
for i in a:
    if i not in b:
        d = a.count(i)
        b += i + str(d)
print(b)
#WAP to get the following output without using count function
a = input("enter a string: ")
b = {}
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
print(b)
#WAP to find the dividers of a number.
a = int(input("Enter a number: "))
for i in range(1,a+1):
    if a % i == 0:
        print(i,end=" ")
#WAP to check the one strinng inside another string.
a = input("Enter a string: ")
b = input("Enter a string: ")
for i in range(len(a)):
    if (a[i:i+len(b):1]) == b:#in slicing the end stop is exclusive
        print(i)
        break
#wap to extract all the non default values from a list
a = eval(input("Enter a List: "))
b = [0,0.0,0j,"",[],{},(),False,set()]
c = []
for i in a:
    if i not in b:
        c += [i]
print(c)
#WAP to get the following output
#ip = 1234567 and op = 2461357
a = int(input("Enter a series: "))
even = ""
odd = ""
for i in str(a):
    if int(i) % 2 == 0:
        even += (i)
    elif int(i) % 2 == 1:
        odd += (i)
print(int(even + odd))
#WAP to find the sum of square of each digit.
a = int(input("Enter a number: "))
b = 0
for i in str(a):
    b += int(i)**2
print(b)
#WAP to extract key value pair only if the key is boolean.
a = eval(input("enter a dict: "))
b = {}
for i in a:
    if type(i) == bool:
        b[i] = a[i]
print(b)
# 71.Wap to print all the integers present in a list.
# 72.Wap to find the length of homogenous tuple without len().
# 73.Wap to extract all the even numbers present in a list.
# 74.Wap to remove duplicates from list
# 75.Wap to reverse a string without using slicing.
# 76.wap to extract all the lowercase characters in a string only if the ascii value is
# even.
a = input("Enter a string: ")
for i in a:
    if ord(i) >= 97 and ord(i) % 2 == 0:
        print(i,end=" ")
# 77.Wap to check whether the last digit of an integer is even or not.
a = int(input("Enter a integer: "))
for i in str(a):
    if int(i) % 2 == 0:
        print(f"{i} the last digit is even")
    else:
        print(f"{i} the last digit is odd")
# 78.Wap to extract all the key value pairs from the dictionary only if the keys are of
# string datatype and values are integers.
a = eval(input("Enter a dict: "))
b = {}
for i in a:
    if type(i) == str and type(a[i]) == int:
        b[i] = a[i]
print(b)
# 79.Wap to extract key value pairs from the dictionary only if both keys and values
# are exactly same.
a = eval(input("Enter a dict: "))
b = {}
for i in a:
    if i == a[i]:
        b[i] = a[i]
print(b)
# 80.Wap to get the following output using len function.
# S=’power star’
# Out={‘power’:5,’star’:4}
a = input("Enter a string: ")
a += " "
word = ""
b = {}
for i in a:
    if i != " ":
        word += i
    else:
        b[word] = len(word)
        word = ""
print(b)
# 81.Wap to get the following output.
# S=’power star’
# Out={‘power’:’rewop’,’star’:’rats’}
a = input("Enter a string: ")
a += " "
word = ""
b = {}
for i in a:
    if i != " ":
        word += i
    else:
        b[word] = word[::-1]
        word = ""
print(b)
# 82. wap to extract all the non default values from a list.
# 83.Wap to check whether the list is homogenous or not.
a = eval(input("Enter a list: "))
b = []
for i in a:
    if type(a[0]) == type(i):
        b.append(i)
    else:
        break
if len(a) == len(b):
    print("it's homogeneous")
# 84.Wap to replace the space by * present in a string
# 85.Wap to count the number of occurrence of a specified character.
a = input("enter a string: ")
b = {}
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
print(b)
# 86. Wap to get the following output.
# S=’always keep smiling’
# Out-‘syawla peek gnilims’
a = input("Enter the string: ")
a += " "
b = ""
for i in a:
    if i != " ":
        b += i
    else:
        print(b[::-1],end=" ")
        b = ""
# 87. Wap to get the following output.
# In=’push maadi kushi padi’
# Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’}
a = input("Enter a string: ")
a += " "
b = ""
c = {}
for i in a:
    if i != " ":
        b += i
    else:
        if len(b) % 2 == 0:
            c[b] = b[0] + b[-1]
        else:
            c[b] = b[len(b)//2]
        b = ""
print(c)
# 88.Wap to toggle a string.
# 89.Wap extract upper, lower, digit and special characters present in a string to different.
# output variable
# 90. Wap to get the following output.
# S=’hai hello ‘
# Out={‘hai’:’ai’,’hello:’eo’}
a = input("Enter a string: ")
b = {}
c = ""
d = ""
for i in a + " ":
    if i != " ":
        c += i
        if i in "AEIOUaeiou":
            d += i
    else:
        b[c] = d
        c = ""
        d = ""
print(b)
# 91. Wap to get the following output.
# S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org’]
# Out=[‘com’,’py’,’html’,’org’]
a = eval(input("Enter the list: "))
b = []
for i in a:
    for j in range(0,len(i)):
        if i[j] == ".":
            b += [i[j+1:len(i)]]
            break
print(b)
# 92. Wap to get the following output.
# S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
# Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],
# ’org’:[‘www’]}
a = eval(input("Enter a List: "))
b = []
c = {}
d = ""
for i in a:
    for j in range(0,len(i)):
        if i[j] == ".":
            b.append(d)
            if i[j+1:len(i)] not in c:
                c[i[j+1:len(i)]] = b
            else:
                c[i[j+1:len(i)]] += b
            b = []
            d = ""
            break
        else:
            d += i[j]
print(c)
# 93.Wap to get the following output.
# L=[‘hai’,34,3.4,’hello’,90,’byebye’]
# Out={‘hai’:’hi’,’hello’:’ho’,’byebye’:’be’}
a = eval(input("Enter a List: "))
b = {}
for i in a:
    if type(i) == str:
        b[i] = i[0] + i[-1]
print(b)
# 94.wap to get the following output.
# In=’hello’
# Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’}
a = input("enter a string: ")
b = {}
for i in range(len(a)):
    b[i] = a[i]
print(b)
# 95.Wap to extract all the string values present in list only if the string is palindrome.
a = eval(input("Enter a List: "))
b = []
for i in a:
    if type(i) == str and i == i[::-1]:
        b.append(i)
print(b)
# 96.Wap to return the positions of vowels present in the given string.
a = input("Enter a string: ")
for i in range(len(a)):
    if a[i] in "AEIOUaeiou":
        print(f"{a[i]}:{i}")
# 97.Wap to check whether the given collection is having nested collection or not.
# 98.Wap to count the number of words in a string.
# 99.Wap to check whether the number is neon number or not.
# N=9→9**2=81→8+1=9
a = int(input("Enter a number: "))
b = 0
for i in str(a**2):
    b += int(i)
if a == b:
    print("Neon")
else:
    print("Not")
# 100.Wap to find the longest word in a string.
a = input("Enter a string: ")
a += " "
b = ""
c = ""
for i in a:
    if i == " " and len(b) < len(c):
        b = c
        c = ""
    elif i == " ":
        c = ""
    else:
        c += i
print(b)
# 101.Wap to replace the special character present in a string by space.
a = input("Enter a string: ")
b = ""
for i in a:
    if "a" <= i <= "z" or "A" <= i <= "Z" or '0' <= i <= '9':
        b += i
    else:
        b += " "
print(b)
# 102.wap to print the square of all the integers present in a list.
a = eval(input("Enter a List: "))
for i in a:
    if type(i) == int:
        print(f"{i}:{i**2}")
# 103.Wap to extract all the odd number present at even index from a list.
a = eval(input("Enter a List: "))
for i in range(len(a)):
    if type(i) == int and a[i] % 2 == 1 and i % 2 == 0 and i != 0:
        print(f"{a[i]}:{i}")
# 104.Wap to extract all the mutable values present in a tuple.
# 105.Wap to get the following output.
# In=’10100011231’
# Out=’010111000’ ( 0→1 and 1→0 if it is other than 0 &1 ignore)
a = int(input("Enter a number: "))
for i in str(a):
    if i in '01':
        print(f"{1-int(i)}",end="")
# 106.Wap to get the following output.
# In=’abacbaacc’
# Out={‘a’:4,’b’:2,’c’:3}
# 107.wap to extract keyvalue pair from the dictionary only if the key is Boolean datatype.
#108.Wap to get the following output.
# In=’127342’
# Out=’242173’ (extract even and odd digits separately and concatenate both)
a = int(input("Enter a number: "))
even = ""
odd = ""
for i in str(a):
    if int(i) % 2 == 0:
        even += i
    else:
        odd += i
print(int(even + odd))
# 109.Wap to checek whether the string is having only lowercase or not using continue.
a = input("Enter a string: ")
b = ""
for i in a:
    if "a" <= i <= "z":
        continue
    else:
        b += i
        break
if len(b) == 1:
    print("have uppercase")
else:
    print("only have lowercase")
# 110.Wap to find the sum square of individual digits of a string.
a = input("Enter a string: ")
b = 0
for i in a:
    if i in "0123456789":
        b += int(i)**2
print(b)
#WAP to check whether the number is perfect or not
a = int(input("enter a number: "))
b = 0
for i in range(1,a):
    if a % i == 0:
        b += i
if a == b:
    print("perfect")
else:
    print("not")
#WAP to inverse a list using a value
a = eval(input("Enter a list: "))
k = int(input("Enter the value of k: "))
for i in range(k):
    a.insert(0,a[-1])
    a.pop()
print(a)
