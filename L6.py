# a = int(input("Enter a number : "))
# count = 0
# while a > 0:
#     a = a // 10
#     count += 1
# print(f"Count of the digits in the number is : {count}")
# a = int(input("Enter the first integer : "))
# b = int(input("Enter the second integer : "))

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("You divided by zero")
# s1 = input("Enter a string : ")
# s2 = input("Enter a character to find in the string : ")
# count = 0
# for i in s1:
#     if i == s2:
#         count+=1
#     else:
#         continue
# if count == 1:
#     print("Character found")
# else:
#     print("Character not found")
# s = "Sai University"
# a = input(("Enter a character to search : "))
# if a in s:
#     print(True)
# if a not in s:
#     print(False)
# s = "Sai University"
# a = input(("Enter a character to search : "))
# if a in s:
#     print(True)
# if a not in s:
#     print(False)
# s = input("Enter a string in lower case :  ") #hello
# s1=""
# for i in s:
#     if ord(i) >= ord('a') and ord(i) <= ord('z'):
#         s1 = s1 + chr(ord(i) - 32)
#     else:
#         s1 = s1 + i
# print(f"The given string in uppercase {s1}")
# a = int(input("Enter a number : "))
# squares = 0
# while a > 0:
#     lastdigit = a % 10
#     v = lastdigit*lastdigit
#     squares += v
#     a = a // 10
# print(f"squares of the digits in the number is : {squares}")
# a = int(input("Enter a number : "))
# sum = 0
# while a > 0:
#     lastdigit = a % 10
#     sum += lastdigit
#     a = a // 10
# print(f"sum of the digits in the number is : {sum}")
# a = int(input("Enter a number : "))
# sum = 0
# while a > 0:
#     lastdigit = a % 10
#     sum += lastdigit
#     a = a // 10
# print(f"sum of the digits in the number is : {sum}")
# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while (i <= n):
#     sum = sum + i
#     i = i + 1
# print("The sum is: ", sum)
#Call by Value

# def change(x):
#     def g(x):
#         x = "Table Tennis"
#         print(x)
#     g(x)  #doubt should ask tommorow
#     x += 1
#     return x

# x = 4
# print(x)
# x = change(x) #if only change(X), it is only call by value
# print(x)
def l1(a):
    i = 0
    count = 0

    while True:
        try:
            char = a[i]
            count += 1
            i += 1
        except IndexError:
            break
    # if count == 1:
    #     print(f"{count} character is present in the given string")
    else:
        print(f"{count} characters are present in the given string")

a = input("Enter a string : ")
l1(a)