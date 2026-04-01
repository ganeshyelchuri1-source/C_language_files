# class circle:
#     def __init__(self,cx=0,cy=0,r=0):
#         self.__cx=cx
#         self.__cy=cy
#         self.__r=r
#     def __str__(self):
#         return f"centre of the circle is ({self.__cx},{self.__cx}) and radius is {self.__r}"
#     def area(self):
#         return f"area={3.14*self.__r*self.__r}"
#     def perimeter(self):
#         return f"perimeter={2*3.14*self.__r}"

# int main() {
# c1=circle(2,3,6)
# print(c1)
# # }
# for i in range(10,0,-1):
#     print(i)
# s = "Sai University"
# for i in range (0, 14, 3):
#     print(s[i], end = " - ") 
#     print(ord(s[i]), end = "    ")

#lecture 6:
# def call(a):
#     num=a
#     count=0
#     while a!=0:
#         count+=1
#         a=a//10
#     return print(count)
# a=int(input("enter a number"))
# # call(a)
# a

# try:  
#     print(a)
# except ValueError:
#     print('it is not defined')
# a = int(input("Enter the first integer : "))
# b = int(input("Enter the second integer : "))

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("You divided by zero")
name=input("enter a sentence")
d=input("enter a word to search")
s=0
for i in name:
    if i==d:
        print("found")
        break
    else:
        continue    #here we can also use pass ,continue both are same but continue will redue the time commplexity
    s+=1
print(s)
