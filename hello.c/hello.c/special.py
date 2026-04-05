# a=input('enter an number')
# #in python when you take input it will come in string
# #a="3"   a is string   => we just want to type cast it to convert into int
# print(a)
# print(type(a))
# a=int(input('enter an number'))
# print(type(a))
# a=int(input("enter a integer"))
# b=int(input("enter a integer"))
# sum=a+b
# print(f"sum is {sum}")
# sub=a-b
# print(f"sub is {sub}")
# pro=a*b
# print(f"pro is {pro}")
# mod=a%b
# print(f"mod is {mod}")
# div=a//b  
# d=a/b     #integer division
# if b>0:
#     print(f"div is {div}")
#     print(f"div is {d}")
# else:
#     print("not possible")
# # print("normal is ",div,"integer is",d)
# # h.w do this interms of float
# a=int(input("enter a integer number"))
# if a%2==0:
#     print("it is even  and divisible by 2")
# else:
#     print("it is odd number")
# a=int(input("enter a number"))
# if a%5==0:
#     print("it is divisible by 5")
# else:
#     print("not divisible by 5")
a=int(input("enter a integer"))
if a%5==0:
    if a%7==0:
        print("it is divisible by 4 and 7")
    else:
        print("it is  divisible by 4 but not 7")
else:
    if a%7==0:
        print("it is not divisible by 5 but divisible by 7" )
    else:
        print("it is not divisible by both 5 and 7")

