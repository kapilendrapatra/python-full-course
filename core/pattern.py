#WAP to print
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        print("*",end=" ")
    print()
#WAP to print a triangle
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()
# **** print this pattern
# *  *
# *  *
# ****
a = int(input("Enter a number: "))
for i in range(a):
    if i == 0 or i == a-1:
        for j in range(a):
            print("*",end=" ")
        print()
    else:
        for j in range(a):
            if j == 0 or j == a-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
# * * * *  print this pattern
# * *   *
# *   * *
# * * * *
a = int(input("Enter a number: "))
for i in range(a):
    if i == 0 or i == a-1:
        for j in range(a):
            print("*",end=" ")
        print()
    else:
        for j in range(a):
            if j == 0 or j == a-1 or i == j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
#WAP to print T shaped * 
a = int(input("Enter a odd number: "))
for i in range(a):
    if i == 0:
        for j in range(a):
            print("*",end=" ")
        print()
    else:
        for j in range(a):
            if j == a//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
# *         * WAP to print this pattern
# * *     * *
# * * * * * *
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if j <= i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(a-1,-1,-1):
        if j <= i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print y
a = int(input("Enter the number: "))
for i in range(1,a+1):
    for j in range(1,a+1):
        if i + j == a+1 or (i == j and i <= a//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print z
n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n or i + j == n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print Y
n = int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i == j and i <= n//2+1) or (i+j == n+1 and i <= n//2+1) or (j == n//2+1 and i >= n//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print A
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a//2 or j == 0 or j == a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print B
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or j == 0 or i == a-1 or (i < a//2 and j == a-1) or (i > a//2 and j == a-1) or (i == a//2+1) or (i == a//2-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print C
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or j == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print D
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or j == 0 or j == a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print E
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or i == a//2 or j == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print F
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a//2 or j == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print G
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or j == 0 or (j == a-1 and i > a//2) or (i == a//2 and j >= a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print H
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == a//2 or j == 0 or j == a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print I
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or j == a//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print J
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or j == a//2 or (i == a-1 and j <= a//2) or (j == 0 and i >= a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print K
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if j == a//2 or (j > a//2 and i+j == a-1) or (j > a//2 and i == j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print L
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == a-1 or j == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print M
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if j == 0 or j == a-1 or (i <= a//2 and j <= a//2 and i == j) or (i < a//2 and j > a//2 and i + j == a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print N
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if j == 0 or j == a-1 or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print o
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or j == 0 or j == a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print P
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or j == 0 or i == a//2 or (i < a//2 and j == a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print Q
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or j == 0 or i == a-1 or j == a-1 or (i > a//2 and j > a//2 and i == j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print R
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a//2 or j == 0 or (i > a//2 and j > a//2 and i == j) or (i < a//2 and j == a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print S
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or i == a//2 or (j == 0 and i < a//2) or (j == a-1 and i > a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print T
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if  j == a//2 or i == 0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print U
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if  j == 0 or i == a-1 or j == a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print V
a = int(input("Enter a number: "))
for i in range(2*a+1):
    for j in range(2*a+1):
        if  (i <= a and j <= a and i == j) or (i < a and j > a and i + j == a*2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print W
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if j == 0 or j == a-1 or (i >= a//2 and i + j == a-1) or (i >= a//2 and i == j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print X
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == j or i + j == a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print Y
a = int(input("Enter a number: "))
for i in range(2*a+1):
    for j in range(2*a+1):
        if  (i <= a and j <= a and i == j) or (i < a and j > a and i + j == a*2) or (i >= a and j == a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print Z
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == 0 or i == a-1 or i + j == a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#WAP to print swastik
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(a):
        if i == a//2 or j == a//2 or (j == 0 and i <= a//2) or (j <= a//2 and i == a-1) or (j == a-1 and i >= a//2) or (i == 0 and j>= a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()




