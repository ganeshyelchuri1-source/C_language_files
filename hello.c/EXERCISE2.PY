# a=int(input("enter a num"))
# b=int(input("enter a num"))
# a=a^b
# b=a^b
# a=a^b
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)
# a=int(input("enter a num"))
# if a%10==0:
#     print("yes")
# else :
#     print("no")
# a=int(input("enter a num"))
# if a&3==0:
#     print("yes")
# a=int(input("enter a num"))
# b=a%10
# if a%3==0:
#     print(f"{a}")
# 
# import math
# a=int(input("enter a num"))
# c=int(input("enter a num"))
# lcm=math.lcm(a,c)
# if lcm==a or lcm==c:
#     print("it happened")
# else:
#     print("not happened")
# a=input("enter a word")
# new=""
# for i in a:
#     if ord(i)>=65 and ord(i)<=90:  doubt =11,
#         i=chr(ord(i)+32)
#         new+=i
#     elif ord(i)>=97 and ord(i)<=122:
#         i=chr(ord(i)-32)
#         new+=i
# print(new)
# a=int(input("enter a year"))
# if a%400==0 and a%100==0 or a%4==0:
#     print("it is possible")
# cost=float(input("enter the cost"))
# sell_prize=float(input("enter the prize to sell"))
# if sell_prize-cost>0:
#     print("profit")
#     print(sell_prize-cost)
#     else:
#         print("loss")
# l=float(input("enter len"))
# b=float(input("enter breadth"))
# area=l*b
# per=2*(l+b)
# print(f"   {area}  {per}")
# time_taken = int(input("Enter time taken to complete the job in minutes: "))
# x1=int(input("enter x1"))
# y1=int(input("enter y1"))
# x2=int(input("enter x2"))
# y2=int(input("enter y2"))
# x3=int(input("enter x3"))
# y3=int(input("enter y3"))
# if y2-y1/x2-x1==y3-y2/x3-x2:
#     print("it will lie on the straight line")
# else:
#     print("not lie on st line")
# x1=int(input("enter  center x1"))
# y1=int(input("enter  center y1"))
# x2=int(input("enter point x1"))
# y2=int(input("enter  point y1"))
# r=int(input("input r value"))
# c=((x2-x1)**2+(y2-y1)**2)**1/2
# d=c-r
# if d>0:
#     print("out side")
# elif d<0:
#     print("in side")
# else:
#     print("on the circle")
# a=int(input("enter x1"))
# s=int(input("enter y1"))
# if a>0 and s>0:
#     print("1")
# elif a>0 and s<0:
#     print("2")
# elif a<0 and s<0:
#     print("3")
# elif a<0 and s>0:
#     print("4")
# elif a==0 and s==0:
#     print("origin")
# elif a==0:
#     print("on y axis")
# else :
#     print("on x axis")
# a=input("enter your health condition")
# age=float(input("enter your age "))
# place=input("enter your place ")
# gender=input("enter your gender")

# if a=="excellent" and (age>=25 and age<=35) and gender=="male" and place=="city":
#     print("4000  and amount 2 lakhs")
# elif a=="excellent" and (age>=25 and age<=35) and gender=="female" and place=="city":
#     print("3000  and amount 1.5 lakhs")
# elif a=="poor" and (age>=25 and age<=35) and place=="village" and gender="male":
#     print("premium is 6000 and cannot exed 1 lakh")
# elif a=="poor" and (age>=25 and age<=35) and place=="village" and gender="female":
#     print("premium is 5000 and cannot exed 1.25 lakh")
# elif age<25 and age>64:
#     printf("not able to registered")
# else:
#     print("propotional to policy value")
# h=int(input("enter hardness value"))
# cc=float(input("enter cc value"))
# ts=float(input("enter ts"))
# if h>=50 and cc<0.7 and ts>5600:
#     print("grade 10")
# elif h>=50 and cc<0.7 :
#     print("grade 9")
# elif cc<0.7 and ts>5600:
#     print("grade 8")
# elif h>=50 or cc<0.7 or ts>5600:
#     print("grade 7")
# else:
#     print("grade")
# s=int(input("e ter how many days "))
# if s<=5:
#     print("50 paise")
# elif s>6 and s<=10:
#     print("1 rupee")
# elif s>10 and s<=30:
#     print("5 rupees")
# else:
#     print("membership cancelled")

# if time_taken <= 30:
#     print("Highly Efficient")
# elif time_taken <= 60:
#     print("Efficient")    19 ,20doubt
# else:
#     print("Needs Improvement")
# a=int(input("enter a number "))
# b=int(input("enter a number "))
# a=a+b
# b=a-b
# a=a+b
# print(f"a value{a}")
# print(f"b value {b}")
# per=float(input("enter marks of your grade "))
# if per>=91 and per<=100:
#     print("S")
# elif per>=81 and per<=90:
#     print("A")
# elif per>=80 and per<=71:
#     print("B")
# elif per>=61 and per<=70:
#     print("C")
# else:
#     print("D")
# x=int(input("enter x value"))
# y=int(input("enter y value"))
# z=int(input("enter z value"))
# if x%y==0:
#     print("x y are possible")
# if x%z==0:
#     print("z x are possible")
# a=int(input("enter a number"))
# if a&1==0:
#     a=a>>2
#     print(f"{a}")
#     print("rem==0")
# else :
#     a=a>>2
#     print(f"{a}")
#     print("rem  1")

# num to hexa decimal
# a=int(input("enter a number"))
# output="123456789ABCDEF"
# res=""
# if a==0:
#     res="0x0"
#     print(res)
# else:
#     while a!=0:
#         b=a%16
#         res=output[b]+res
#         a=a//16
#         print(f"out put{res}")
# num to binary
# a=int(input("enter a number"))
# output="01"
# res=""
# if a==0:
#     res="0"
#     print(res)
# else:
#     while a!=0:
#         b=a%2
#         res=output[b]+res
#         a=a//2
#     print(f"out put{res}")
# binary to decimal
# a=int(input("enter a num in binary"))
# num=0
# b=0
# count=0
# while a!=0:
    
#     b=a%10
#     if b==0:
#         num+=0
#     else:
#         num+=b*(2**count)
#     count+=1
#     a=a//10
# print(f"{num}")
# binary to integer
# a=int(input("enter a num in hex"))
# str="12345678ABCDEF"
# num=0
# b=0
# count=0
# while a!=0:
    
#     b=a%10
#     if b==0:
#         num+=0
#     else:
#         num+=b*(2**count)
#     count+=1
#     a=a//10
# print(f"{num}")
