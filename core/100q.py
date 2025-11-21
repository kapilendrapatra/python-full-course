# Q1.Write a program to print the following using while loop
# First 10 Even numbers
i=1
while i<=10:
    print(2*i,end=' ')
    i+=1    
# Q2.First 10 Odd numbers
i=0
while i<10:
    print(2*i+1,end=' ')
    i+=1
# Q3. First 10 Natural numbers
i=1
while i<=10:
    print(i,end=' ')
    i+=1
# Q4. First 10 Whole numbers
i=0 
while i<10:
    print(i,end=' ')
    i+=1
# Q5. Write a program to print first 10 integers and their squares using while loop.
i=1
while i<=10:
    print(f"{i} {i**2}")
    i+=1
# Q6. Write while loop statement to print the following series: 10, 20, 30 ... ... 300
i=1
while i<=30:
    print(10*i,end=' ')
    i+=1
# Q7. Write a while loop statement to print the following series 105, 98, 91 .........7.
i=0
while i<15:
    print(105-7*i,end=' ')
    i+=1
# Q8. Write a program to print the first 10 natural number in reverse order using while loop.
i=10
while i>0:
    print(i,end=' ')
    i-=1
# Q9. Write a program to print sum of first 10 Natural numbers.
i=1
sum=0
while i<=10:
    sum+=i
    i+=1
print(sum)
# Q10. Write a program to print sum of first 10 Even numbers.
i=1
sum=0
while i<=10:
    sum+=2*i
    i+=1
print(sum)
# Q11. Write a program to print table of a number entered from the user.
n=int(input('enter the num:'))
i=1
while i<=10:
    print(f"{n}*{i}={n*i}")
    i+=1
# Q12. Write a program to print all even numbers that falls between two numbers (exclusive
# both numbers) entered from the user using while loop.
n1=int(input('enter the first num:'))
n2=int(input('enter the second num:'))
i=n1+1
while i<n2:
    if i%2==0:
        print(i,end=' ')
    i+=1
# Q13. Write a program to check whether a number is prime or not using while loop.
a = int(input("Enter the number: "))
b,i = 0,2
while i < a:
    if a % i == 0:
        b += 1
    i += 1
if b == 0:
    print("Prime")
else:
    print("Not prime")
# Q14. Write a program to find the sum of the digits of a number accepted from the user.
a = int(input("Enter the number: "))
b = 0
while a > 0:
    b += a%10
    a = a//10
print(b)
# Q15. Write a program to find the product of the digits of a number accepted from the user.
n=int(input('enter the num:'))
prod=1
while n>0:
    r=n%10
    prod*=r
    n=n//10
print(prod)
# Q16. Write a program to reverse the number accepted from user using while loop.
a = int(input("Enter a number: "))
b = 0
while a > 0:
    b = b*10 + a%10
    a = a//10
print(b)
# Q17. Write a program to display the number names of the digits of a number entered by
# user, for example if the number is 231 then output should be Two Three One
n=int(input('enter the num:'))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
while rev>0:
    r=rev%10
    if r==0:
        print('Zero',end=' ')
    elif r==1:
        print('One',end=' ')
    elif r==2:
        print('Two',end=' ')
    elif r==3:
        print('Three',end=' ')
    elif r==4:
        print('Four',end=' ')
    elif r==5:
        print('Five',end=' ')
    elif r==6:
        print('Six',end=' ')
    elif r==7:
        print('Seven',end=' ')
    elif r==8:
        print('Eight',end=' ')
    elif r==9:
        print('Nine',end=' ')
    rev=rev//10
# Q18. Write a program to print the Fibonacci series till n terms (Accept n from user) using
# while loop
a = int(input("enter the number till fibonacci series: "))
i,p,q = 0,0,1
while i < a:
    print(p,end=" ")
    p,q = q,p+q
    i += 1
#.Q19. Write a program to print the factorial of a number accepted from user.
n=int(input('enter the num:'))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)
# Q20. Write a program to check whether a number is Armstrong or not. (Armstrong number is
# a number that is equal to the sum of cubes of its digits for example : 153 = 1^3 + 5^3 + 3^3.)
n=int(input('enter the num:'))
sum=0
temp=n
while n>0:
    r=n%10
    sum+=r**3
    n=n//10
if sum==temp:
    print('armstrong')
else:
    print('not armstrong')
# Q21. Write a program to add first n terms of the following series using a while loop:
# 1/1! + 1/2! + 1/3! + ........ + 1/n!
n=int(input('enter the num:'))
i=1
sum=0
fact=1
while i<=n:
    fact*=i
    sum+=1/fact
    i+=1
print(sum)
# Q22. Write a program to enter the numbers till the user wants and at the end it should
# display the sum of all the numbers entered.
sum = 0
while True:
    a = eval(input("Enter the number: "))
    if type(a) == int:
        sum += a
    else:
        break
print(sum)
# Q23. Write a program to enter the numbers till the user enter ZERO and at the end it should
# display the count of positive and negative numbers entered.
pos,neg = 0,0
while True:
    num = int(input("Enter the numbers: "))
    if num == 0:
        break
    elif num > 0:
        pos += 1
    else:
        neg += 1
print(f"the numbers of positive is {pos} and negative is {neg}")
# Q24. Write a program to find the HCF of two numbers entered from the user.
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
hcf,i = 0,1
while i <= b:
    if a%i == 0 and b%i == 0 and i > hcf:
        hcf = i
    i += 1
print(hcf)
# Q25. Write a program to convert Decimal to Binary.
n=int(input('enter the num:'))
bin=0
place=1
while n>0:
    r=n%2
    bin=bin+r*place
    place*=10
    n=n//2
print(bin)
# Q26. Write a program to convert Binary to Decimal.
n=int(input('enter the num:'))
dec=0
place=0
while n>0:
    r=n%10
    dec=dec+r*(2**place)
    place+=1
    n=n//10
print(dec)
# Q27. Write a program to check whether a number is palindrome or not.
a = int(input("enter the number: "))
b = a
c = 0
while b > 0:
    c = (c*10) + (b%10)
    b = b//10
if c == a:
    print("palindrome")
else:
    print("Not palindrome")
# Q28. Write a python program to sum the sequence:
# 1 + 1/1! + 1/2! + 1/3! + ........ + 1/n!
n=int(input('enter the num:'))
i=1
sum=1
fact=1
while i<=n:
    fact*=i
    sum+=1/fact
    i+=1
print(sum)
# Q29. Write a program to accept 10 numbers from the user and display it’s average
i=1
sum=0
while i<=10:
    n=int(input('enter the num:'))
    sum+=n
    i+=1
print(sum/10)
# Q30. Write a program to accept 10 numbers from the user and display the largest & smallest
# number number.
i=1
largest=-999999
smallest=999999
while i<=10:
    n=int(input('enter the num:'))
    if n>largest:
        largest=n
    if n<smallest:
        smallest=n
    i+=1
print(f"largest={largest} smallest={smallest}")
# Q31. Write a program to display sum of odd numbers and even numbers separately that fall
# between two numbers accepted from the user.(including both numbers) using while loop.
n1=int(input('enter the first num:'))
n2=int(input('enter the second num:'))
i=n1
sumo=0
sume=0
while i<=n2:
    if i%2==0:
        sume+=i
    else:
        sumo+=i
    i+=1
print(f"sume={sume} sumo={sumo}")
# Q32. Write a program to display all the numbers which are divisible by 13 but not by 3
# between 100 and 500.(exclusive both numbers)
i=101
while i<500:
    if i%13==0 and i%3!=0:
        print(i,end=' ')
    i+=1

# Q33. Write a program to print the following series till n terms.
# 2 , 22 , 222 , 2222 _ _ _ _ _ n terms
n=int(input('enter the num:'))
i=1
num=2
while i<=n:
    print(num,end=' ')
    num=num*10+2
    i+=1
# Q34. Write a program to print the following series till n terms.
# 1 4 9 16 25 _ _ _ _ _ n terms.
n=int(input('enter the num:'))
i=1
while i<=n:
    print(i**2,end=' ')
    i+=1
# Q35. Write a program to find the sum of the following series(accept values of x and n from
# user)
# 1 + x/1! + x2/2! + ..........xn/n!
x=int(input('enter the x:'))
n=int(input('enter the n:'))
i=1
sum=1
fact=1
x_pow=1
while i<=n:
    fact*=i
    x_pow*=x
    sum+=x_pow/fact
    i+=1
print(sum)
# Q36. Write a program to find the sum of following series :
# x + x2/2 + ..........xn/n
x=int(input('enter the x:'))
n=int(input('enter the n:'))
i=1
sum=0
x_pow=x
while i<=n:
    sum+=x_pow/i
    x_pow*=x
    i+=1
print(sum)
# Q37. Write a program to find the sum of following series
# 1 + 8 + 27 ............n terms
n=int(input('enter the num:'))
i=1
sum=0
while i<=n:
    sum+=i**3
    i+=1
print(sum)
# Q38. Write a program to find the sum of following series:
# 1 + 2 + 6 + 24 + 120 . . . . . n terms
n=int(input('enter the num:'))
i=1
sum=0
fact=1
while i<=n:
    fact*=i
    sum+=fact
    i+=1
print(sum)
# Q39. Write a program to find the sum of following series:
# S = 1 + 4 – 9 + 16 – 25 + 36 – ... ... n terms
n=int(input('enter the num:'))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum+=i**2
    else:
        sum-=i**2
    i+=1
print(sum)
# Q40. Write a Program to print all the characters in the string ‘PYTHON’ using while loop.
s='PYTHON'
i=0
while i<len(s):
    print(s[i])
    i+=1
# Q41. Write a program to print only odd numbers from the given list using while loop. L = [23,
# 45, 32, 25, 46, 33, 71, 90]
L = [23, 45, 32, 25, 46, 33, 71, 90]
i=0
while i<len(L):
    if L[i]%2!=0:
        print(L[i],end=' ')
    i+=1
# Q42. Write a program to print all the factors of a number using while loop.
n=int(input('enter the num:'))
i=1
while i<=n:
    if n%i==0:
        print(i,end=' ')
    i+=1
# Q43. Write a python program to get the following output
# 1—–49
# 2—–48
# 3—–47
# ...
# ...
# 48—–2
# 49—–1
i=1
j=49
while i<=49 and j>=1:
    print(f"{i}----{j}")
    i+=1
    j-=1
# Q44.Write a program to extract all the upper case character from the given string
# s=input(‘enter the string:’)
s=input('enter the string:')
i=0
while i<len(s):
    if s[i].isupper():
        print(s[i],end=' ')
    i+=1
# Q45.Write a Program to separate positive and negative number from a list.
# x = eval(input('enter the list:'))
x = eval(input('enter the list:'))
i=0
pos=[]
neg=[]
while i<len(x):
    if x[i]>=0:
        pos.append(x[i])
    else:
        neg.append(x[i])
    i+=1
print(f"positive={pos} negative={neg}")
# Q46.Write a program that appends the type of elements from a list.
# n = [23, 'Python',23.98]
n = [23, 'Python',23.98]
i=0
types=[]
while i<len(n):
    types.append(type(n[i]))
    i+=1
print(types)
# Q47. Write a program to fetch only even values from a dictionary.
# dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 }
dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 }
even_values=[]
for key in dic:
    if dic[key]%2==0:
        even_values.append(dic[key])
print(even_values)
# Q48.Write a program to extract all the string data items from the given list only
# if string is palindrome
l = ['python', 'madam', 23, 'radar', 45.89, '12321']
i=0
palindromes=[]
while i<len(l):
    if type(l[i])==str:
        if l[i]==l[i][::-1]:
            palindromes.append(l[i])
    i+=1
print(palindromes)
# Q49.Write a program to extract all the special characters from the given string
s=input('enter the str:')
i=0
special_chars=[]
while i<len(s):
    if not s[i].isalnum() and s[i]!=' ':
        special_chars.append(s[i])
    i+=1
print(special_chars)
# Q50.Write a program to extract all the upper case character ,lower case
# character ,numbers and special characters into four different output variables
# from the given string
s=input('enter the str:')
i=0
upper=[]
lower=[]
digits=[]
special=[]
while i<len(s):
    if "A" <= s[i] <= "Z":
        upper.append(s[i])
    elif "a" <= s[i] <= "z":
        lower.append(s[i])
    elif "0" <= s[i] <= "9":
        digits.append(s[i])
    else:
        special.append(s[i])
    i+=1
print(f"upper={upper} lower={lower} digits={digits} special={special}")
# Q51.Write a program to get the following output
# input=’abcd’
# output=’a1b2c3d4’
s=input('enter the str:')
i=0
output=''
while i<len(s):
    output+=s[i]+str(i+1)
    i+=1
print(output)

# Q52.Write a program to convert all the lower case charater to upper case
# characters present in a given string
s=input('enter the str:')
i=0
output=''
while i<len(s):
    if "a" <= s[i] <= "z":
        output+=chr(ord(s[i])-32)
    else:
        output+=s[i]
    i+=1
print(output)
# Q53.Write a program to convert all the lower case character to upper case
# character and upper case character to lower case character by keeping number
# and special character as it is
s=input('enter the str:')
i=0
output=''
while i<len(s):
    if "a" <= s[i] <= "z":
        output+=chr(ord(s[i])-32)
    elif "A" <= s[i] <= "Z":
        output+=chr(ord(s[i])+32)
    else:
        output+=s[i]
    i+=1
print(output)
# Q54.Write a program to extract all the lower case character from the given
# string only if its ascii value is even
s=input('enter the str:')
i=0
output=''
while i<len(s):
    if "a" <= s[i] <= "z":
        if ord(s[i])%2==0:
            output+=s[i]
    i+=1
print(output)
# Q55.Write a program to get the following output
# input=’abcd’
# output={‘a’:97,’b’:98,’c’:99,’d’:100}
s=input('enter the str:')
i=0
output={}
while i<len(s):
    output[s[i]]=ord(s[i])
    i+=1
print(output)
# Q56.Write a program to get the following output
# input=’hello’
# output={0:’h’ , 1:’e’ , 2:’l’ , 3:’l’ , 4:’o’}
s=input('enter the str:')
i=0
output={}
while i<len(s):
    output[i]=s[i]
    i+=1
print(output)
# Q57.Write a program to get the following output
# input=[‘hai’ , 89 ,3.4 , ‘hello’ , 90 , ‘py’]
# output={‘hai’:’hi’ , ‘hello’:’ho’ , ‘py’:’py’}
a = eval(input("enter the list: "))
b = {}
for i in a:
    if type(i) == str:
        b[i] = (i[0]+i[-1])
print(b)
# Q58.Write a program to get the following output
# input=‘hai hello’
# output=’olleh iah’
s=input('enter the str:')
print(s[::-1])
# Q59.write a program to count the number of vowels present in a given string
s=input('enter the str:')
i=0
count=0
vowels='aeiouAEIOU'
while i<len(s):
    if s[i] in vowels:
        count+=1
    i+=1
print(count)
# Q60.Write a program to get the following output
# input=‘hai hello good morning’
# output={‘hai’:’a’ , ‘hello’: ‘l’ , ‘good’:’gd’ , ‘morning’:’n’}
a = input("enter a string: ").split()
b = {}
for i in a:
    if len(i)%2 != 0:
        b[i] = i[len(i)//2]
    else:
        b[i] = (i[0] + i[-1])
print(b)
# Q61.Write a program to get the following output
# input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’]
# output=[‘com’ , ’py’ , ‘html’]
a = eval(input("enter the list: "))
b = []
for i in a:
    for j in range(len(i)):
        if i[j] == ".":
            b += [i[j+1:]]
print(b)
# Q62.Write a program to get the following output
# input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’ , ‘amazon.com’ , ‘text.py’]
# output={‘com’:[‘jiocinema’ , ‘amazon’] , ’py’:[ ‘file’ , ‘text’]
# , ‘html’:[‘web’]}
a = eval(input("enter the list: "))
b = {}
for i in a:
    temp = i.split(".")
    if temp[1] not in b:
        b[temp[1]] = [temp[0]]
    else:
        b[temp[1]] += [temp[0]]
print(b)
# Q63.Write a program to get the following output(count no of vowels)
# input=’hai hello’
# output={‘hai’:2 , ‘hello’:2}
a = input("enter a string: ").split()
b = []
for i in a:
    c = 0
    for j in i:
        if j in "aeiou":
            c += 1
    b += [f"'{i}':{c}"]
print(b)
# Q64.Write a program to extract all the string values present in the list collection
# only if the last character is upper case. Concatenate the extracted output using
# ‘*’
l = ['hai' , 89 ,3.4 , 'Hello' , 90 , 'pyT']
i=0
output=[]
while i<len(l):
    if type(l[i])==str and 'A' <= l[i][-1] <= 'Z':
        output.append(l[i])
    i+=1
print('*'.join(output))
# Q65.write a program to extract all the list data items present in list collection
# only if it is having middle value , that value is integer and having even number
# at start
a = eval(input("Enter the List: "))
for i in a:
    if type(i) == list:
        if len(i)%2 == 1 and type(i[0]) == int:
            print(i)
# Q66.Write a program to get the following output
# input= ‘just looking like wow’
# output= ‘jusT LOOKING Like a wow’
s=input('enter the str:').split()
i=0
output=[]
while i<len(s):
    if len(s[i])%2==0:
        new_word=s[i][:-1]+s[i][-1].upper()
        output.append(new_word)
    else:
        new_word=s[i][:len(s[i])//2]+s[i][len(s[i])//2].upper()+s[i][len(s[i])//2+1:]
        output.append(new_word)
    i+=1
print(' '.join(output))
# Q67.Program to find the common elements in two sets using a while loop
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
a = eval(input("enter first set: "))
b = eval(input("enter second set: "))
a = list(a)
b = list(b)
c = []
for i in range(len(a)):
    if a[i] in b and a[i] not in c:
        c += [a[i]]
print(set(c))
# Q68.Program to check if a number is a perfect number or not using while loop
a = int(input("Enter the number: "))
b,i= 0,1
while i < a:
    if a%i == 0:
        b += i
    i += 1
if a == b:
    print("perfect")
else:
    print("Not perfect")
# Q69.Program to find the length of the longest substring without repeating
# characters in a given string
a = input("Enter a string: ")
lon = ""
temp = ""
for i in a:
    if i not in temp and i != " ":
        temp += i
    elif i == " ":
        if len(temp) > len(lon):
            lon = temp
        temp = ""
        
print(lon,len(lon),sep=":")
# Q72.Program to find the maximum and minimum elements in a tuple
a = eval(input("enter a tuple: "))
max = -10000000000
min = 10000000000
for i in a:
    if max <= i:
        max = i
    elif i <= min:
        min = i
print(f"the maximum is {max} and the minimum is {min}")
# Q73.Program to find the union, intersection, and difference of two sets using while
# loop

# Q74.Program to count the number of occurrences of each character in a string using
# a dictionary and while loop
a = input("Enter a string: ")
b = {}
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
print(b)
# Q75.Write a program to remove duplicate value from collection without converting to set
a = eval(input("enter a collection: "))
b = []
for i in a:
    if i not in b:
        b += [i]
    else:
        b.remove(i)
print(b)
# Q76.Write a program to find the length of collection without using len function
a = eval(input("Enter a list: "))
c = 0
for i in a:
    c += 1
print(f"the length of the list is {c}")
# Q77.Write a program to extract all the integers from a list only if the integer is starting from
# even number and ending as odd number and having length more than 3
a = eval(input("Enter a List: "))
for i in a:
    if type(i) == int and len(str(i)) >= 3 and str(i)[0] in "24680" and i%2 == 1:
        print(i,end=",")
# Q78.Write a program to extract all the individual data items of a list if the length of extracted
# output is more than 4 print the first value of the output else print last value of the output list
# and add 10 to it
l = [[12, 23, 34], [45, 56], [67, 78, 89, 90], [11, 22, 33, 44, 55], [66]]
i=0
output=[]
while i<len(l):
    j=0
    while j<len(l[i]):
        output.append(l[i][j])
        j+=1
    i+=1
if len(output)>4:
    print(output[0])
else:
    print(output[-1]+10)
# Q79.Write a program to get the following output
# input1=’11001010’
# input2=’01110010’
# output=4(to count how many positions are having same value)
a = input("enter 5 digits: ")
b = input("enter 5 digits: ")
c = 0
for i in range(len(a)):
    if a[i] == b[i]:
        c += 1
print(c)    
# Q80..Write a program to get the following output
# input=[1,2,3,4,5,6]
# value=3
# output=[1,2,3][4,5,6]
# If value=2
# output=[1,2][3,4][5,6]
a = eval(input("Enter a list: "))
b = int(input("Enter a value: "))
for i in range(0,len(a),b):
        print(a[i:(i+b)],end=" ")
# Q81..Write a program to check weather the given number is spy number or not
# i.e, 1*2*3=1+2+3
a = int(input("enter the number: "))
sum = 0
prod = 1
while a > 0:
    sum += (a%10)
    prod *= (a%10)
    a //= 10
if sum == prod:
    print("spy")
else:
    print("Not spy")
# Q82.Write a program to check weather the given number is Xylem number or
# not i.e, 1234 → 1+4=2+3
a = int(input("Enter the number: "))
end = 0
bet = 0
for i in range(len(str(a))):
    if i == 0 or i == len(str(a))-1:
        end += int(str(a)[i])
    else:
        bet += int(str(a)[i])
if end == bet:
    print('Xylem')
else:
    print("Not Xylem")
# Q83.Write a program to check weather the given number is phloem number or
# not
# I.e, 12345→ 1+5!=2+3+4
n=int(input('enter the num:'))
s=str(n)
i=0
first_sum=0
second_sum=0
while i<len(s)//2:
    first_sum+=int(s[i])
    i+=1
j=len(s)-1
while j>len(s)//2:
    second_sum+=int(s[j])
    j-=1
if first_sum!=second_sum:
    print('phloem number')
else:
    print('not phloem number')
# Q84.Write a program to check weather the given number is neon number or not
# i.e. 9 is number, 9**2=81→8+1=9
n=int(input('enter the num:'))
square=n**2
sum=0
while square>0:  
    sum+=square%10
    square=square//10
if sum==n:
    print('neon number')
else:
    print('not neon number')

# Q85.Write a program to check weather the given number is automorphic or not
# I.e.5 is number 5**2=25 last digit of 25 is the number itself
a = int(input("Enter a number: "))
b = a**2
for i in range(len(str(b))+1):
    if str(b)[-1] == str(a):
        print("automorphic")
        break
    else:
        print("not automorphic")
        break
# Q86.Write a program to count number of words in the given string
# s=input('enter the str:').split()
s=input('enter the str:').split()
i=0
count=0
while i<len(s):
    count+=1
    i+=1
print(count)
# Q87.Write a program to find the length of the longest word
a = input("enter a string: ").split()
c = 0
for i in a:
    if len(i) > c:
        c = len(i)
print(c)
# Q88.Write a program to count number of consonants in the given string
# s=input('enter the str:')
a = input("enter a string: ")
b = 0
for i in a:
    if "A" <= i <= "Z" or "a" <= i <= "z":
        if i not in "AEIOUaeiou":
            b += 1
print(b)

# Q89.Write a program to check the type of data entered by the users
data=input('enter the data:')
if data.isdigit():
    print('integer')
elif data.replace('.','',1).isdigit() and data.count('.')<2:
    print('float')
elif data.isalpha():
    print('string')
elif data.isalnum():
    print('alphanumeric')
else:
    print('special character')
# Q90.Write a program to check weather the given tuple is palindrome or not
a = eval(input("enter a tuple: "))
if a == a[::-1]:
    print("pallindrome")
else:
    print("not a pallindrome")
# Q91.Write a program to check weather the given collection is having nested
# collection or not
l = [1, 2, [3, 4], 5]
i=0
has_nested=False
while i<len(l):
    if type(l[i])==list or type(l[i])==tuple or type(l[i])==set or type(l[i])==dict:
        has_nested=True
        break
    i+=1
if has_nested:
    print('having nested collection')
else:
    print('not having nested collection')
# Q92. Write a program to return the positions of vowels present in the given
# string
s=input('enter the str:')
i=0
positions=[]
vowels='aeiouAEIOU'
while i<len(s):
    if s[i] in vowels:
        positions.append(i)
    i+=1
print(positions)
# Q93:Write a program to find length of collection without using len function
a = eval(input("Enter a collection: "))
count = 0
for i in a:
    count += 1
print(count)
# Q94.Write a program to whether the entered username and password is correct
# or not if not correct print enter again
username='admin'
password='admin123'
while True:
    user=input('enter the username:')
    pwd=input('enter the password:')
    if user==username and pwd==password:
        print('login successful')
        break
    else:
        print('enter again')
# Q95.Write a program to extract all integer data items from tuple
t = (12, 'hello', 23.5, 45, 'world', 67)
i=0
integers=[]
while i<len(t):
    if type(t[i])==int:
        integers.append(t[i])
    i+=1
print(integers)
# Q96.Write a program to extract all the non default values from the list
l = [0, "", None, 23, "hello", 45.6, [], {}, 67]
i=0
non_default=[]
while i<len(l):
    if l[i] not in (0, "", None, [], {}, ()):
        non_default.append(l[i])
    i+=1
print(non_default)
# Q97.Write a program to get the following output -
# Input='hai hello how are you'
# output='hai**hello**how**are**you'
a = input("Enter a string: ")
b = ""
for i in a:
    if i == " ":
        b += "**"
    else:
        b += i
print(b)
# Q98.Write a program to reverse the given list
a = eval(input("Enter a list: "))
print(a[::-1])
# Q99.Write a program for number game
import random
number=random.randint(1,100)
while True:
    guess=int(input('enter your guess between 1 to 100:'))
    if guess<number:
        print('too low')
    elif guess>number:
        print('too high')
    else:
        print('congratulations you guessed it right')
        break

# Q100.Write a program to print ‘Thank you’ for n times
n=int(input('enter the num:'))
i=1
while i<=n:
    print('Thank you')
    i+=1