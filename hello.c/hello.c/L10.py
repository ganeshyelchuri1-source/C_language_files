# class complex:
#     def __init__(self,x,y):#constructor(special method)
#         self.x=x
#         self.y=y
#     def details(self):#method
#         print(f"{self.x}+{self.y}i")

#     def add(self,others):
#         others.x=self.x+others.x
#         #c2.x=c1.x+c2.x
#         others.y=self.y+others.y
#         return others
#     def sub(self,others):
#         others.x=self.x-others.x
#         #c2.x=c1.x+c2.x
#         others.y=self.y-others.y
#         return others
#     def mag(self,others):
#         others.x=(others.x**2+others.y**2)**1/2
#         others.y=(self.y**2+self.y**2)**1/2
#         return others 
# c1=complex(1,2)
# c1.details()
# c2=complex(3,2)
# c2.details()
# c1=c1.add(c2)
# c1.details()
# c1=c1.mag(c2)
# c2.details()
# class person:
#     def __init__(self,name,age,height,gender):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.gender=gender
#     def __str__(self):#why this __str__was created is it a constructor
#         return f"name :{self.name} height:{self.height} gender:{self.gender} age={self.a}"
#     def ageupdate(self,age):
#         self.age=age#here comes the real usage of this oops concept because privacy data can be updatad easily 

# s1=person("abc",19,170,"m")
# s1.ageupdate(21)#how did this dot operator works
# print(s1)# in this condition age is updated 
# class person:
#     def __init__(self,name,age,height,gender):
#         self.__name=name# due to the usage of self.__name=name here due to usage of this extra __ atrributes got the ability
#         self.__age=age   #private attributes   so we can say that
#         self.__height=height
#         self.__gender=gender
#         # self.count=0    normal attributes
#     def __str__(self):
#         return f"name :{self.__name} height:{self.__height} gender:{self.__gender} age={self.__age}"

#     def update(self,Age=None,Height=None):
#         if Age is not None:#here none acts as nULL
#             self.age=Age
#         if Height is not None:
#             self.height=Height
#         # self.age=value
# s1=person("abc",19,170,"m")
# print(s1)

# s1.update(Age=22,Height=467) # about this code from 53 to 64
# print(s1)
# # print(s1.height)
# print(s1)
# class person:

#     def __init__(self, name, age, gender, height):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.height = height
#     def person_details(self):
#         print(f"Name : {self.name} | Age : {self.age} | Gender : {self.gender} | Height : {self.height} ")
#     def update(self, new_age, new_height):
#         self.age = new_age
#         self.height = new_height

# p1 = person("Person1", 18, "M", 180)
# p1.person_details()
# p1.update(20, 185)
# p1.update(70,67)
# p1.gender="female"
# p1.name="no name"
# p1.person_details()
#Multiplication
# class complex:
#     def __init__(self, x, y): #Constructor ( Special Method )
#         self.x = x
#         self.y = y
#     def details(self): #Method
#         print(f"{self.x} + {self.y}i")
#     def mult(self, others):
#         self.real=real
#         self.imag=imag
#         real = (self.x * others.x) - (self.y * others.y)
#         imag = (self.x * others.y) + (self.y * others.x)
#         self.real=real
#         self.imag=imag
#         return self.real,self.imag
# c1 = complex(1,2)
# c1.details()
# c2 = complex(3,2)
# c2.details()
# c1 = c1.mult(c2)
# c1.details()



# types of try and except casess
# try:
#     print(a)
# except NameError:
#     print("not found")

# a="ganesh"
# for i in range(0,100):
#     try:
#         print(a[i])
#     except IndexError:
#         print("not possible")