class complex:
    def __init__(self,x,y):#constructor(special method)
        self.x=x # whenever we are creating an object this method gets call automatically
        self.y=y
    def details(self):#method
        print(f"{self.x}+{self.y}i")

    def add(self,others_object):
        # others_object.x=self.x+others_object.x
        # #c2.x=c1.x+c2.x
        # others_object.y=self.y+others_object.y
        real  = self.x + others_object.x
        img = self.y+others_object.y#when we want to return simply real and imaginary  they are not belongs to the class
        # complex but when we write this return complex(real,img) here they are converted into the class complex this works just like type castinghhj
        
        return complex(real,img)
    def sub(self,others):
        others.x=self.x-others.x
        #c2.x=c1.x+c2.x
        others.y=self.y-others.y
        return others
    def mul(self,others):
        real=self.x*others.x-self.y*others.y
        imaginary=self.x*others.y+self.y*others.x
        return complex(real,imaginary)
    def div(self,others):
        division=((self.x+self.y)/(others.x+others.y))*((others.x-others.y)/(others.x-others.y))
        return complex(division,0)

c1=complex(1,2)
c1.details()
c2=complex(3,2)
c2.details()
c1=c1.add(c2)
c1.details()
c1=c1.sub(c2)
c1.details()
c1=c1.mul(c2)
c1.details()

c1=c1.div(c2)
c1.details
# c1,c2 are objects    complex is the class
"""
class complex:
    def __init__(self,x,y):#constructor(special method)
        self.x=x
        self.y=y
    def details(self):#method
        print(f"{self.x}+{self.y}i")

    def mul(self,others):
        others.x=self.x*others.x
        #c2.x=c1.x+c2.x
        others.y=self.y*others.y
        c2.y=c2.y*c1.y
        return others
          real=self.x*others.x-self.y*others.y
          imaginary=self.x*others.y+self.y*others.x
          return complex(real,imaginary)
    def sub(self,others):
        others.x=self.x-others.x
        #c2.x=c1.x+c2.x
        others.y=self.y-others.y
        return others
    def mul(self,others):
        real=(others.x*self*x)-(self.u*others.y)
        image=(self.x*others.y)+(self.y*others.x)
        return complex(real,imag)

c1=complex(1,2)
c1.details()
c2=complex(3,2)
c2.details()
# c1=c1.add(c2)
c1=c1.add(c2)
c1.details()
print(type(c1))
class student:
    def __init__(self,name,id,cgpa):
        self.name=name
        self.id=id
        self.cgpa=cgpa
    def student_details(self):
        return f"Name {self.name},id {self.id} and cgpa:{self.cgpa}"
    def update_cgpa(self,new_cgpa):
        self.cgpa=new_cgpa

s1=student("xyz",21,7.4)
s2=student("abc",30,5.9)
# print(s1.student_detail())
print(s2.student_detail())
s2.update_cgpa(8.3)
print(s2.student_detail())
class complex:
    def __init__(self,name,age,gender,height):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
    def complex_details(self):
        return f"name {self.name} age {self.age} gender {self.gender} height {self.height}"

s1=complex("xyz",25,"male",5.8)
print(s1.name)"""
# print(s1.age)
# print(s1.complex_details())
# print(s1.gender)
# print(s1.height)
"""class complex:
    # def __init__(self,a,b):
        self.a=a
        self.b=b
    def details(self):
        return f"{(self.a)}+{(self.b)}i"
    def add(self,others):
        self.a=self.a+others.a
        self.b=self.b+others.b
        return self
    def sub(self,others):
        self.a=others.a-self.a
        self.b=others.b-self.b
        return self
    def mul(self,others):
        real=self.a*others.a-self.b*others.b
        imaginary=self.b*others.a+self.a*others.b
        return complex(real,imaginary)


c1=complex(10,3)
print(c1.details())
c2=complex(3,7)
print(c2.details())
c1=c1.add(c2)
print(c1.details())
c1=c1.sub(c2)
print(c1.details())
c1=c1.mul(c2)
print(c1.details())
print(c1)"""

