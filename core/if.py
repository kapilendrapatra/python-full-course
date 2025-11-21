# 2. Wap to check whether the character is vowel or not.
a = input("Enter a character: ")
if a in 'aeiouAEIOU':
    print(f"{a} is a vowel")
else:
    print(f"{a} is not a vowel")
# 3. Wap to print Ascii value of a character only if it is upper case.
a = input("Enter a character: ")
if 'A' <= a <= 'Z':
    print(f"The ASCII value of {a} is {ord(a)}")
else:
    print(f"{a} is not an uppercase letter")
# 4. Wap to print the cube of a number only if it is divisible by 9 or 6.
a = int(input("Enter a number: "))
if a % 9 == 0 or a % 6 == 0:
    print(f"The cube of {a} is {a**3}")
else:
    print(f"{a} is not divisible by 9 or 6")
# 5. Wap to check whether the given integer is 3 Digit number.
a = input("Enter an integer: ")
if len(a) == 3:
    print(f"{a} is a 3-digit number")
else:
    print(f"{a} is not a 3-digit number")
# 6. Wap to check whether the last digit of a given number is 5.
a = input("Enter a number: ")
if a[len(a)-1] == '5':
    print(f"The last digit of {a} is 5")
else:
    print(f"The last digit of {a} is not 5")
# 7. Wap to check whether the given data is float.
a = eval(input("Enter a data: "))
if type(a) == float:
    print(f"{a} is a float")
else:
    print(f"{a} is not a float")
# 8. Wap to check whether the data is single value data.
a = eval(input("Enter a data: "))
if type(a) == int or type(a) == float or type(a) == str or type(a) == bool or type(a) == complex:
    print(f"{a} is a single value data")
else:
    print(f"{a} is not a single value data")
# 9. Wap to check whether the given character is digit or not. 
a = eval(input("Enter a character: "))
if type(a) == int or type(a) == float:
    print(f"{a} is a digit")
else:
    print(f"{a} is not a digit")