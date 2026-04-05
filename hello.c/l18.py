# #coin question
# def call(amount):
    
# l=[1,2,5]
# amount=10
# call(amount)


# s=[1,2,3]   
# if isinstance(s,list):  # checks that(var,data) data type of var is same as data type
#     print("it is a list")#not isinstance(s,list)
# else:
#     print("it is not a list")



# s='saiuniversity'
# if s.isalpha():
#     print("it is alphabets")
# else:
#     print(" not  all an alphabets")



# s="123445"
# if s.isnumeric():#s.isdigit()  both acts as same
#     print("all are digits")
# else:
#     print("all are not digits")


# s='mourya1234'
# if s.isalnum():
#     print("word contain digits and alphabets")
# else:
#     print("may be there is any special character")


# try:
#     a=int(input("enter a number"))
#     b=int(input("enter another number"))
#     c=a//b
# except ZeroDivisionError:
#     print("you are dividing it with zero!")
# else:
#     print("resulst",c)
# finally:
#     print("code runned correctly without any error")
# s="abc"
# try:
#     print(f"{s[6]}")
# except IndexError:        #what is different between function and method?
#     print("not possible")
# print("execution completed")

# try:
#     s=input("enter a number")
# except IndexError:  #when we did not metion any kind of error it is no problem  it will work but when u written any type it will work only for that
#     print("it is not possible")
# else:
#     print(f"{s[0]}")

# finally:
#     print("it is completed")
# try:
#     import math
#     a=int(input("enter a number to find its root"))

# except ValueError:
#         # b=abs(a)
#         print(f"{math.sqrt(-a)}")
# else:
#     print(f"result,{math.sqrt(-a)}")
# finally:
#      print("program done sucessfully")


try:
    import math
    a=input("enter a number to find its root")

except TypeError:
    a=int(a)
    print("it is an integer")
except ValueError:
        # b=abs(a)
        print(f"{math.sqrt(-a)}")
else:
    print(f"result,{math.sqrt(-a)}")
finally:
     print("program done sucessfully")
