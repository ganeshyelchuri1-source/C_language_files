"""class person:
    def __init__(self,name,age,height,gender):
        self.__name=name
        self.__age=age   #private attributes
        self.__height=height
        self.__gender=gender
        # self.count=0    normal attributes
    def __str__(self):
        return f"name :{self.__name} height:{self.__height} gender:{self.__gender} age={self.__age}"
    def update(self,Age=None,Height=None):
        if Age is not None:
            self.age=Age
        if Height is not None:
            self.height=Height
        # self.age=value
    def __gt__(self,other_object):
        return self.__age>other_object.__age#__gt__ is an inbuilt method
    def __gt__(self,other_object):
        return self.__height>other_object.__height
    def ageupdate(self,updateage):
        self.__updatedage=updateage
        return updateage
s1=person("abc",19,1,"m")
print(s1)
s1.age=50
print(s1)

s1.update(Age=22,Height=467)
print(s1.age)
s2=person("ncw",34,162,"m")
print(s2)
print(s1>s2)#s1.>s2
print(s1>s2)
#you are giving new meaning to s1>s2  this is called as overloading(appling the concept on new members)
# print(s1.height)
print(s1)"""

class complex:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    # def add(self,others_object):
       # c1=complex
    #     c1.x=self.x+others_object.x
    #     c1.y=self.y+others_object.y
    #     return c1
    def __add__(self,others_object):# why did we use this __name__
        c1=complex()
        c1.x=self.x+others_object.x
        c1.y=self.y+others_object.y
        return c1
    def __mul__(self,others_object):
        # c1=complex()
        real=self.x*others_object.x-self.y*others_object.y
        imaginary=others_object.x*self.y+others_object.y*self.x
        return complex(real,imaginary)
    def detail(self):
        print(f"{self.x}+i{self.y}")
c1=complex(1,2)
c1.detail()
c2=complex(3,2)
c2.detail()
# c3=c1.mul(c2)   # operator overloading
c3= c1*c2
c3.detail()
c3=c1+c2
c3.detail()
# how many symbols can we overload and we cannot overload
# class my_list:
#     def __init__(self):
#         self.l=[0,0,0,0,0,0,0,0]
#         self.count=0
#     def my_append(self,value):
#         self.value=value
#         self.l[self.count]=self.value
#         self.count=self.count+1
#     def print_list(self):
#         print("[",end="")
        
#         for i in range(0,self.count):
#             print(self.l[i],end=" ")
#         print("]",end="") 
#     def pop(self):
#         name=self.l[self.count-1]
#         self.count=self.count-1
#         return name  #in the  list enter a element at certain position,,same as delete  as  h.w
#     def push(self):
#         p=int(input("enter a number"))
#         self.p=p
#         self.count+=1
#         self.l[self.count-1]=self.p
#         name=self.l[self.count-1]
#         return name
#     def insertatposition(self):
#         p=int(input("enter a position"))
#         self.p=p
#         self.count+=1
#         # count=self.count
#         put=int(input("enter an element"))
#         self.put=put
#         for i in range(self.count,p,-1):
#             self.l[i] = self.l[i-1]
#             #how to run the for loop reverse
#         self.l[p]=self.put
# l1= my_list()
# l1.my_append(4)
# l1.my_append(7)
# l1.my_append(3)
# l1.my_append(2)
# l1.my_append(1)
# l1.print_list()
# print(l1.pop())
# l1.print_list()
# l1.push()
# l1.print_list()
# l1.insertatposition()
# l1.print_list()