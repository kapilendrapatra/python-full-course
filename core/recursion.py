'''steps to convert a looping into recursion
1.initialization of all the variables should be done at the time of function declaration.
2.the termination condition should be exactly opposite to the looping condition.
3.return the total output inside termination condition.
4.logic of the program should be same as looping.
5.updation of the looping variable should be done at the end of recursive call.'''
#for loop can't be recursive but while loop can be recursive.

# 39.Wap to print python for 5 times.
def p(i):
    if i == 0:
        return 0
    print("python")
    p(i-1)
p(i = 5)
# 40.Wap to print n natural numbers.
def natural(n,i=1):
    if i > n:
        return 0
    print(i)
    natural(n,i+1)
natural(int(input("Enter: ")))
# 41.Wap to print multiplication table for n.
def multi(n=int(input("Enter a number: ")),i=1):
    if i > 10:
        return 0
    print(f"{n} * {i} = {n*i}")
    multi(n,i+1)
multi()

# 45.Wap to print all the characters present at even index of a string.
def string(a,out='',i=0):
    if i >= len(a):
        print(out)
        return 0
    if i % 2 == 0 and i != 0:
        out += a[i]
    string(a,out,i+1)
string(input("enter the string: "))
# 46.Wap to extract all the lowercase characters present in a string.
def string(a,out='',i=0):
    if i > len(a)-1:
        print(out)
        return 0
    if 97 <= ord(a[i]) <= 122:
        out += a[i]
    string(a,out,i+1)
string(input("Enter a string: "))
# 47.Wap to extract all the vowels present in a string.
def string(s,out='',i=0):
    if i >= len(s):
        return out
    if s[i] in 'AEIOUaeiou':
        out += s[i]
    string(s,out,i+1)
print(string(input("Enter a string: ")))
# 48.Wap to print factors of a integer number.
def fact(a,i=1):
    if i > a:
        return 0
    if a % i == 0:
        print(i,end=",")
    fact(a,i+1)
fact(int(input("Enter the number: ")))
# 49.Wap to toggle a string.
def togg(a,i=0):
    if i >= len(a):
        return 0
    if 65 <= ord(a[i]) <= 91:
        print(a[i].lower(),end="")
    elif 97 <= ord(a[i]) <= 122:
        print(a[i].upper(),end="")
    else:
        print(a[i],end="")
    togg(a,i+1)
togg(input("enter the string: "))
# 50.Wap to reverse the given number.
def rev(a,i):
    if i == -1:
        return 0
    print(a[i],end='')
    rev(a,i-1)
a = int(input("Enter a number: "))
b = len(str(a))-1
rev(str(a),b)
# 51.Wap to find the sum of individual digits of a number.
def sum(a,s=0,i=0):
    if i > len(a)-1:
        print(s)
        return 0
    s += int(a[i])
    sum(a,s,i+1)
sum(str(int(input("enter a number: "))))

# 55.Wap to extaract all the even integers present in a tuple at odd index.
def wow(a,out=[],i=0):
    if i >= len(a):
        print(out)
        return out
    if i % 2 != 0 and a[i] % 2 == 0 and type(a[i]) == int:
        out += [a[i]]
    wow(a,out,i+1)
wow(eval(input("Enter a tuple: ")))