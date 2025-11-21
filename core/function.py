# 121.Wap to check whether the number is strong or not.
a = int(input("Enter the number: "))
b = 0
def strong(a):
    s = 1
    for i in range(1,a+1):
        s *= i
    return s
for i in str(a):
    b += strong(int(i))
if b == a:
    print("Strong")
else:
    print("Not strong")
# 122.Wap to print the strong numbers between the given range.
print("Enter the range: ")
a = int(input())
b = int(input())
def strong(a,b):
    for i in range(a+1,b):
        s = 0
        for j in str(i):
            c = 1
            for k in range(1,int(j)+1):
                c *= k
            s += c
        if s == i:
            print(i,end=" ")
strong(a,b)
# 123.Wap to find the nth strong number.
def abc(a):
    prod = 1
    for i in range(a,0,-1):
        prod *= i
    return prod
a = int(input("Enter the end: "))
for i in range(1,a+1):
    sum = 0
    for j in str(i):
        sum += abc(int(j))
    if sum == i:
        print(i,end=",")
# 124.Wap to check whether the number is arm strong or not.
def armstrong(a):
    sum = 0
    for i in a:
        sum += (int(i) ** len(a))
    if sum == int(a):
        print("Armstrong")
    else:
        print("Not")
armstrong(str(int(input("Enter a number: "))))
# 125.Wap to print the arm strong numbers between the given range.
def armstrong(a):
    sum = 0
    for i in a:
        sum += int(i) ** len(a)
    if sum == int(a):
        print(a,end=",")
a = int(input("Enter the start: "))
b = int(input("Enter the end: "))
for i in range(a,b+1):
    armstrong(str(i))
# 126.Wap to find the nth arm strong number.
def armstrong(a):
    sum = 0
    for i in a:
        sum += int(i) ** len(a)
    if sum == int(a):
        print(a,end=",")
b = int(input("Enter the end: "))
for i in range(b+1):
    armstrong(str(i))
# 127.Wap to check whether the number is perfect or not.
def perfect(a):
    sum = 0
    for i in range(1,a):
        if a % i == 0:
            sum += i
    if a == sum:
        print("Perfect")
    else:
        print("Not")
perfect(int(input("Enter the number: ")))
# 128.wap to print the perfect numbers between the given range.
def perfect(a):
    sum = 0
    for i in range(1,a):
        if a % i == 0:
            sum += i
    if sum == a:
        print(a,end=",")
a = int(input("Enter the start: "))
b = int(input("Enter the end: "))
for i in range(a,b+1):
    perfect(i)
# 129.Wap to find the nth perfect number.
def perfect(a):
    sum = 0
    for i in range(1,a):
        if a % i == 0:
            sum += i
    if sum == a:
        print(a,end=",")
b = int(input("Enter the end: "))
for i in range(1,b+1):
    perfect(i)
# 130.Wap to check whether the number is prime or not.
def prime(a):
    count = 0
    for i in range(2,a):
        if a % i == 0:
            count += 1
    if count == 0:
        print("Prime")
    else:
        print("Not")
prime(int(input("Enter the number: ")))
# 131.wap to print the prime numbers between the given range.
def prime(a):
    sum = 0
    for i in range(2,a):
        if a % i == 0:
            sum += 1
            break
    if sum == 0:
        print(a,end=",")
a = int(input("enter the start: "))
b = int(input("enter the end: "))
for i in range(a,b+1):
    prime(i)
# 132.Wap to find the nth prime number.
def prime(a):
    sum = 0
    for i in range(2,a):
        if a % i == 0:
            sum += 1
            break
    if sum == 0:
        print(a,end=",")
b = int(input("enter the end: "))
for i in range(1,b+1):
    prime(i)
# 133.Wap to check whether the number is Fibonacci number or not.
def fibonacci(a):
    b,c = 0,1
    for i in range(a+1):
        if b > a:
            print("Not in fibonacci series")
            break
        elif b == a:
            print("it's in fibonacci series")
            break
        b,c = c,b+c
fibonacci(int(input("Enter the number: ")))
# 134.wap to print the Fibonacci numbers between the given range.
def fibonacci(a,d):
    b,c = 0,1
    for i in range(d+1):
        if b > d:
            break
        elif b > a:
            print(b,end=",")
        b,c = c,b+c
fibonacci(int(input("Enterr the start: ")),int(input("Enter the end: ")))
# 135.Wap to find the nth Fibonacci number.
def fibonacci(d):
    b,c = 0,1
    for i in range(d+1):
        if b > d:
            break
        else:
            print(b,end=",")
        b,c = c,b+c
fibonacci(int(input("Enter the end: ")))
# 136.Wap to check whether the number is palindrome or not.
def palindrome(a):
    if a == a[::-1]:
        print("Palindrome")
    else:
        print("Not")
palindrome(str(int(input("Enter the number: "))))
# 137.wap to print the palindrome numbers between the given range.
def palindrome(a):
    if a == a[::-1]:
        print(int(a),end=",")
a = int(input("enter the start: "))
b = int(input("enter the end: "))
for i in range(a,b+1):
    palindrome(str(i))
# 138.Wap to find the nth palindrome number.
def palindrome(a):
    if a == a[::-1]:
        print(a,end=",")
a = int(input("Enter the end number: "))
for i in range(1,a+1):
    palindrome(str(i))
# 139.Wap to check whether the number is happy number or not.
b = int(input("Enter the number: "))
def happy(a):
    if len(str(a)) > 1:
        sum = 0
        for i in str(a):
            sum += int(i) ** 2
        if sum == 1:
            print("happy")
        else:
            happy(sum)
    else:
        if a == 1:
            print("happy")
        else:
            print("Not")
happy(b)
# 140.wap to print the happy numbers between the given range.
def happy(c):
    if len(c) > 1:
        sum = 0
        for i in c:
            sum += int(i) ** 2
        if sum == 1:
            print(a,end=",")
        else:
            happy(str(sum))
for i in range(int(input("Start: ")),int(input("End: "))):
    a = i
    happy(str(i))
# 141.Wap to find the nth happy number.
def happy(c):
    if len(c) > 1:
        sum = 0
        for i in c:
            sum += int(i) ** 2
        if sum == 1:
            print(a,end=",")
        else:
            happy(str(sum))
for i in range(int(input("End: "))):
    a = i
    happy(str(i))
# 142.wap to check whether the string is anagram or not.
def anagram(a,b):
    if len(a) == len(b):
        for i in a:
            c = 0
            if i not in b:
                print("Not anagram")
                break
            else:
                c = 1
    else:
        print("Not anagram")
    if c == 1:
        print("Anagram")
anagram(input("Enter the first word:").lower(),input("Enter the second word:").lower())
# 143.Wap to check whether the string is pangram or not.
def panagram(a):
    for i in range(97,123):
        if chr(i) not in a:
            print("it's not panagram")
            return 0
    return 1
c = panagram(input("Enter your string: ").lower())
if c == 1:
    print("it's panagram")
# 144.Wap to check whether the number is xylem or not.
# Ex: 1234→1+4=2+3
a = int(input("Enter a number: "))
def xylem():
    sum1 = 0
    sum2 = 0
    for i in range(len(str(a))):
        if i == 0 or i == len(str(a))-1:
            sum1 += i
        else:
            sum2 += i
    if sum1 == sum2:
        print("Xylem")
    else:
        print("Not")
xylem()
# 145.Wap to check whether the number is spy or not.
# Ex: 123→1+2+3=1*2*3
a = int(input("Enter the number: "))
def spy(a):
    sum = 0
    prod = 1
    for i in str(a):
        sum += int(i)
        prod *= int(i)
    if sum == prod:
        print("Spy")
    else:
        print("Not")
spy(a)