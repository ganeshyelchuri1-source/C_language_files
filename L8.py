# def call(a):
#     str="abcdefghijklmnopqrstuvwxyz"
#     count=0
#     for i in a:
#         if i in str:
#             count+=1
#     return count



# a=input("enter a number")
# print(call(a))


# def call():
#     count=0
#     for i in a:
#         count+=1
#     print(count)

# a=input("enter  a word")
# call()
# def length(s):
#     count=0.
#     while True:
#         try:
#             chr=s[i]
#             i+=1
#             count+=1
#         except IndexError:
#             break
#     print(f"counting is{count} ")
#     s=input("enter a string")
#     length(s)
# def call(a):
#     count=0
#     for i in range(0,100):
#         if a!=0:
#             a=a//10
#             count+=1
#         else:
#             break
#     print(f"num={count}")

# a=int(input("enter a number"))
# call(a)
# def call(a):
#     count=0
#     while a!=0:
#         a=a//10
#         count+=1
#     return count

# a=int(input("enter a number"))
# print(f"no.of digits={call(a)}")
# we are writing the code by considering the object

#syntax of class
# class cylinder:
#     def __init__(self,h,r):          #constructor(is a special type of method)
#         self.he= h#atttributer or datd member 
#         self.ra= r#atttributer or datd member 
#         def volume(self): #member function or method
#             return 3.14*self*he*self.ra*self.ra
#         def surface_area(self): #member function or method
#             return 2*3.14*self.he*self.ra


# c1 = cylinder(1,1)
# c2 = cylinder(2,2) #instance
# #hw to call a method on c1
# print(c1.volume())

# c1=college("ganesh",34,456)
# # print(c1)
# print(c1.iq())
# print(c1.place())
# print(c1.details())
# class complex:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sec(self):
#         return "top"
#     def detail(self):
#         return f"name = {self.name} age = {self.age}"
# s1=complex("ganesh",18)
# print(s1.detail())
# a="ganesh"
# for i in range(0,20):
#     Try:
#         print(i)
#     Except IndexError:
#         print("not space")
# a="ganesh"
# # b=int(input("enter"))
# for i in range(0,20):
#     try:
#         print(i)
#     except:
#         print("not possible")
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
    if count == 1:
        print(f"{count} character is present in the given string")
    else:
        print(f"{count} characters are present in the given string")

a = input("Enter a string : ")
l1(a)

