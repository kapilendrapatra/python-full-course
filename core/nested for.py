# 111. Wap to get the following output. without length function.
# S=’power star’
# Out={‘power’:5,’star’:4}
a = input("enter a string: ")
a += " "
b = {}
c = ""
for i in a:
    if i == " ":
        d = 0
        for j in c:
            d += 1
        b[c] = d
        c = ""
    else:
        c += i
print(b)
# 112. Wap to get the following output.
# S=’power star’
# Out={‘power’:2,’star’:1} (no of vowels is key)
a = input("Enter a string: ")
b = {}
c = ""
for i in (a + " "):
    if i == " ":
        d = 0
        for j in c:
            if j in "AEIOUaeiou":
                d += 1
        b[c] = d
        c = ""
    else:
        c += i
print(b)
# 113. Wap to get the following output.
# S=’kabab is love’
# Out={‘kabab’:[‘babak’,2,’kbb’],’is’:[‘si’,1,’i’],’love’:[‘evol’,2,’lv’]}
# [reverse,no of vowels,char at even index]
a = input("Enter a string: ")
a += " "
b = {}
c = ""
e = ""
for i in range(len(a)):
    if a[i] == " ":
        d = 0
        if c not in b:
            b[c] = [c[::-1]]
            for j in range(len(c)):
                if c[j] in "AEIOUaeiou":
                    d += 1
                
                if j % 2 == 0:
                    e += c[j]
            b[c] += [d]
            b[c] += [e]
            e = ""
            c= ""
    else:
        c += a[i]
print(b)
# 114. Wap to get the following output.
# S=’kabab is love’
# Out={‘kb’:(‘kbb’,3,’bbk’),’is’:(‘s’,1,’s’),’le’:(‘lv’,2,’vl’)}
# { 1st+last char: (consonant,no of consonant,rev of consonant)}
a = input("enter a string: ")
b = {}
d = ""
nr = ""
for i in a + " ":
    if i != " " and i not in "AEIOUaeiou" and i not in nr:
        nr += i 
    elif i != " " and i not in "AEIOUaeiou":
        d += i
    elif i == " ":
        b[nr] = [(nr + d)]
        b[nr] += [len(str(nr) + str(d))]
        b[nr] += [(nr + d)[::-1]]
        d = ""
        nr = ""
print(b)
# 115.Wap to get the following output.
# In=[100,200,35,40,60]
# Out=[335,235,400,395,375] (total sum-value)
a = eval(input("Enter a List: "))
b = []
for i in a:
    sum = 0
    for j in a:
        if i != j:
            sum += j
    b += [sum]
print(b)
# 116. Wap to get the following output.
# In=’bacbcaabbaa’
# Out=’b4a5c2’
a = input("Enter a strinng: ")
b = ""
for i in a:
    count = 0
    if i not in b:
            b += i
            for j in a:
        
                if i == j:
                    count += 1
            print(f"{i}{count}",end="")
# 117. Wap to get the following output
# In=[100,200,50,400,300]
# N=300
# Out=[[100,200],[300]]
# 118.Wap to check whether the number is strong or not.
# 119.Wap to get the following output.
# In={10:’star’,20:’bye’,30:’moon’,40:’apple’}
# Out={10:’a’,20:’e’,30:’oo’,40:’ae’}
a = eval(input("Enter a dict: "))
b = {}
for i in a:
    s = ""
    for j in a[i]:
        if j in "AEIOUaeiou":
            s += j
    b[i] = s
print(b)
# 120. Wap to get the following output.
# In=[‘hello’,227,3.4,’last’,189,34]
# Out=[722,981,43]
a = eval(input("enter the List: "))
b = []
for i in a:
    if type(i) == int:
        b.append(int(str(i)[::-1]))
print(b)
#WAP to find the length of string with out len function
a = input("Enter a string: ")
c = {}
b = ""
for i in a + " ":
    d = 0
    if i != " ":
        b += i
    else:
        for j in b:
            d += 1
        c[b] = d
        b = ""
print(c)
#WAP to verify whether a number is strong or not
a = int(input("Enter a number: "))
b = 0
for i in str(a):
    p = 1
    for j in range(1,int(i)+1):
        p *= j
    b += p
if a == b:
    print("strong")
else:
    print("not")