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
n=int(input('enter the num:'))
i=2
flag=0
while i<=n//2:
    if n%i==0:
        flag=1
        break
    i+=1
if flag==0:
    print('prime')
else:
    print('not prime')
# Q14. Write a program to find the sum of the digits of a number accepted from the user.
n=int(input('enter the num:'))
sum=0
while n>0:
    r=n%10
    sum+=r
    n=n//10
print(sum)
# Q15. Write a program to find the product of the digits of a number accepted from the user.
n=int(input('enter the num:'))
prod=1
while n>0:
    r=n%10
    prod*=r
    n=n//10
print(prod)
# Q16. Write a program to reverse the number accepted from user using while loop.
n=int(input('enter the num:'))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print(rev)
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
# while loop.Q19. Write a program to print the factorial of a number accepted from user.
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
sum=0
while True:
    n=int(input('enter the num:'))
    sum+=n
    ch=input('do you want to continue y/n:')
    if ch.lower()=='n':
        break
print(sum)
# Q23. Write a program to enter the numbers till the user enter ZERO and at the end it should
# display the count of positive and negative numbers entered.
pos=0
neg=0
while True:
    n=int(input('enter the num:'))
    if n>0:
        pos+=1
    elif n<0:
        neg+=1
    else:
        break
print(f"positive={pos} negative={neg}")
# Q24. Write a program to find the HCF of two numbers entered from the user.
n1=int(input('enter the first num:'))
n2=int(input('enter the second num:'))
i=1
hcf=1
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        hcf=i
    i+=1
print(hcf)
# Q25. Write a program to convert Decimal to Binary.
n=int(input('enter the num:'))
a=0
b=1
while n>0:
    r=n%2
    a=a+r*b
    b*=10
    n=n//2
print(a)
# Q26. Write a program to convert Binary to Decimal.
n=int(input('enter the num:'))
a=0
b=0
while n>0:
    r=n%10
    a=a+r*(2**b)
    b+=1
    n=n//10
print(a)
# Q27. Write a program to check whether a number is palindrome or not.
n=int(input('enter the num:'))
rev=0
temp=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==temp:
    print('palindrome')
else:
    print('not palindrome')
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
largest=0
smallest=0
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
    print(num,end=' ,')
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
l=['hai' , 89 ,3.4 , 'hello' , 90 , 'py']
i=0
output={}
while i<len(l):
    if type(l[i])==str:
        output[l[i]]=l[i][0]+l[i][-1]
    i+=1
print(output)
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
s=input('enter the str:').split()
i=0
output={}
while i<len(s):
    if len(s[i])%2==0:
        output[s[i]]=s[i][0]+s[i][-1]
    else:
        output[s[i]]=s[i][len(s[i])//2]
    i+=1
print(output)
# Q61.Write a program to get the following output
# input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’]
# output=[‘com’ , ’py’ , ‘html’]
input_list=['jiocinema.com' , 'file.py' , 'web.html']
output_list=[]
i=0
while i<len(input_list):
    part=input_list[i].split('.')
    output_list.append(part[1])
    i+=1
print(output_list)
# Q62.Write a program to get the following output
# input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’ , ‘amazon.com’ , ‘text.py’]
# output={‘com’:[‘jiocinema’ , ‘amazon’] , ’py’:[ ‘file’ , ‘text’]
# , ‘html’:[‘web’]}
input_list=['jiocinema.com' , 'file.py' , 'web.html' , 'amazon.com' , 'text.py']
output_dict={}
i=0
while i<len(input_list):
    part=input_list[i].split('.')
    key=part[1]
    value=part[0]
    if key in output_dict:
        output_dict[key].append(value)
    else:
        output_dict[key]=[value]
    i+=1
print(output_dict)
# Q63.Write a program to get the following output(count no of vowels)
# input=’hai hello’
# output={‘hai’:2 , ‘hello’:2}
s=input('enter the str:').split()
i=0
output={}
vowels='aeiouAEIOU'
while i<len(s):
    count=0
    j=0
    while j<len(s[i]):
        if s[i][j] in vowels:
            count+=1
        j+=1
    output[s[i]]=count
    i+=1
print(output)
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
l = [[2,4,6] , [1,3,5] , [2,3,4] , [11,22,33] , [44,55,66] , [10,20,30]]
i=0
output=[]
while i<len(l):
    if len(l[i])%2!=0:
        mid_index=len(l[i])//2
        if type(l[i][mid_index])==int and l[i][0]%2==0:
            output.append(l[i])
    i+=1
print(output)
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
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
common_elements=[]
list1=list(set1)
i=0
while i<len(list1):
    if list1[i] in set2:
        common_elements.append(list1[i])
    i+=1
print(common_elements)
# Q68.Program to check if a number is a perfect number or not using while loop
n=int(input('enter the num:'))
i=1
sum=0
while i<=n//2:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print('perfect number')
else:
    print('not perfect number')
# Q69.Program to find the length of the longest substring without repeating
# characters in a given string using while loop
s=input('enter the str:')
i=0
longest=''
while i<len(s):
    j=i
    temp=''
    while j<len(s):
        if s[j] not in temp:
            temp+=s[j]
        else:
            break
        j+=1
    if len(temp)>len(longest):
        longest=temp
    i+=1
print(len(longest))
# Q72.Program to find the maximum and minimum elements in a tuple using while
# loop
t = (23, 45, 67, 12, 89, 5, 90)
i=0
maximum=-999999
minimum=999999
while i<len(t):
    if t[i]>maximum:
        maximum=t[i]
    if t[i]<minimum:
        minimum=t[i]
    i+=1
print(f"maximum={maximum} minimum={minimum}")
# Q73.Program to find the union, intersection, and difference of two sets using while
# loop
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Q74.Program to count the number of occurrences of each character in a string using
# a dictionary and while loop
s=input('enter the str:')
i=0
output={}
while i<len(s):
    if s[i] in output:
        output[s[i]]+=1
    else:
        output[s[i]]=1
    i+=1
print(output)
# Q75.Write a program to remove duplicate value from collection without converting to set
l = [10, 20, 30, 10, 20, 40, 50]
i=0
output=[]
while i<len(l):
    if l[i] not in output:
        output.append(l[i])
    i+=1
print(output)
# Q76.Write a program to find the length of collection without using len function
l = [10, 20, 30, 10, 20, 40, 50]
i=0
count=0
while i<len(l):
    count+=1
    i+=1
print(count)
# Q77.Write a program to extract all the integers from a list only if the integer is starting from
# even number and ending as odd number and having length more than 3
l = [123, 2345, 6789, 456, 8907, 1234, 56789]
i=0
output=[]
while i<len(l):
    str_num=str(l[i])
    if len(str_num)>3 and str_num[0] in '02468' and str_num[-1] in '13579':
        output.append(l[i])
    i+=1
print(output)
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
input1='11001010'
input2='01110010'
i=0
count=0
while i<len(input1) and i<len(input2):
    if input1[i]==input2[i]:
        count+=1
    i+=1
print(count)    
# Q80..Write a program to get the following output
# input=[1,2,3,4,5,6]
# value=3
# output=[1,2,3][4,5,6]
# If value=2
# output=[1,2][3,4][5,6]
input_list=[1,2,3,4,5,6]
value=int(input('enter the value:'))
i=0
output=[]
while i<len(input_list):
    temp=[]
    j=0
    while j<value and i<len(input_list):
        temp.append(input_list[i])
        i+=1
        j+=1
    output.append(temp)
print(output)
# Q81..Write a program to check weather the given number is spy number or not
# i.e, 1*2*3=1+2+3
n=int(input('enter the num:'))
prod=1
sum=0
while n>0:
    r=n%10
    prod*=r
    sum+=r
    n=n//10
if prod==sum:
    print('spy number')
else:
    print('not spy number')
# Q82.Write a program to check weather the given number is Xylem number or
# not i.e, 1234 → 1+4=2+3
n=int(input('enter the num:'))
s=str(n)
i=0
first_sum=0
second_sum=0
while i<len(s)//2:
    first_sum+=int(s[i])
    i+=1
j=len(s)-1
while j>=len(s)//2:
    second_sum+=int(s[j])
    j-=1
if first_sum==second_sum:
    print('xylem number')
else:
    print('not xylem number')   
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
    r=square%10
    sum+=r
    square=square//10
if sum==n:
    print('neon number')
else:
    print('not neon number')

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
s=input('enter the str:').split()
i=0
longest=''
while i<len(s):
    if len(s[i])>len(longest):
        longest=s[i]
    i+=1
print(len(longest))
# Q88.Write a program to count number of consonants in the given string
# s=input('enter the str:')
s=input('enter the str:')
i=0
count=0
vowels='aeiouAEIOU'
while i<len(s):
    if s[i].isalpha() and s[i] not in vowels:
        count+=1
    i+=1
print(count)

# Q89.Write a program to check the type of data entered by the users
data=input('enter the data:')
if type(data) == int:
    print('integer')
elif type(data) == str:
    print('string')
elif type(data) == float:
    print("float")
else:
    print('special character')
# Q90.Write a program to check weather the given tuple is palindrome or not
a = eval(input("enter a tuple : "))
if a == a[::-1]:
    print("palindrome")
# Q91.Write a program to check weather the given collection is having nested
# collection or not
a = eval(input("enter a list : "))
i = 0
while(i < len(a)):
    if type(a[i]) == list or type(a[i]) == tuple or type(a[i]) == set or type(a[i]) == dict:
        print("nested")
        break
    i += 1
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
l = [10, 20, 30, 10, 20, 40, 50]
i=0
count=0
while i<len(l):
    count+=1
    i+=1
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
s=input('enter the str:').split()
i=0
output=''
while i<len(s):
    output+=s[i]
    if i!=len(s)-1:
        output+='**'
    i+=1
print(output)
# Q98.Write a program to reverse the given list
l = [10, 20, 30, 40, 50]
i=len(l)-1
rev=[]
while i>=0:
    rev.append(l[i])
    i-=1
print(rev)
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
#WAP to show the input is palindrome or not without using slicinng method
a = eval(input("Enter a string: "))
l,r,i = 0,len(a),0
while l < r:
    if a[l] != a[r-1]:
        i = 0
        break
    else:
        i = 1
    l += 1
    r -= 1
if i != 0:
    print("palindrome")
else:
    print("Not palindrome")
#WAP to use simple number search game
import random
a = random.randint(1,100)
while True:
    b = int(input("Enter a number: "))
    if b > a:
        print("number should be small")
    elif a > b:
        print("number should be big")
    else:
        print("you got your number")
        break
#WAP to use binary number search game
import random
a = random.randint(1,100)
b = int(input("Enter a number: "))
while True:
    if b > a or a > b:
        b = (b+a)//2
    else:
        print(f"{b} is your random number")
        break
#WAP to make a simple hand cricket game
import random
score = 0
while True:
    c = (0,1,2,3,4,5,6)
    d = int(input("Enter a number: "))
    if random.choice(c) == d:
        print(score)
        break
    else:
        score += d
#WAP to find the number of valid paranthesis
a = input("Enter a paranthesis pattern: ")
b = 0
i,j = 0,0
while i < len(a):
    if a[i] == "(":
        if a[i+1] == ")":
            j += 1
    i += 1
print(j)
