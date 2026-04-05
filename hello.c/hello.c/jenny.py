# # a="1234"
# # print(type(a))
# # # print(len(a))
# # b=a[0]
# # d=a[1]
# # c=int(d)+int(b)
# # print(c)
# who will pay the bill
# import random
# a=input("enter the members of the party")
# l=a.split(" ")
# print(l)
# c=random.choice(l)
# print(c)
# saving money at particular position in sape of matrix 3*3
# money=float(input("enter the money to enter in the place"))
# place=input("enter the place value:")
# a,b=place.split(" ")
# c=int(a)
# d=int(b)
# list=[[1,1,1],[1,1,1],[1,1,1]]
# list[c-1][d-1]=money
# print(type(list))

# print(list[0])
# print(list[1])
# print(list[2])
# a=input("enter the row and coloumn position")
# money=float(input("enter the money to enter"))
# c,d=a.split(" ")
# i=int(c)
# j=int(d)
# list=[[1,1,1],[1,1,1],[1,1,1]]
# list[int(i-1)][int(j-1)]=money
# print(list[0])
# print(list[1])
# print(list[2])
#rock paper sizors problem
# import random
# u=int(input("enter a thing rock0 paper1  sizors2"))
# u
# d=random.randint(0,3)
# print(d)
# if d==2 and u==0:
#     print("you won")
# elif d==0 and u==2:
#     print("you lose")
# elif d==u:
#     print("tie better luck next time")
# elif d>u:
#     print("you lose")
# elif d<u:
#     print("you won")
# else:
#     print("invalid")
# printing list with numbers
# numbers=[1,2,3,4,5,6,7,8]
# square=[]
# for i in numbers:
#     d=i*i
    
#     square.append(d)
# print(square)   
# # heigt checker
# a=input("enter the height  values orderly")

# list=a.split(" ")
# count=0
# for i in list:
#     count+=1
#     print(list)
# for i in range(count-1):
#     list[i]=int(list[i])
# d=0
# sum=0
# for i in list:
#     sum=sum+list[i]
#     d+=1
# total=sum//d
# sum of even from 1 to 100
# sum=0
# for i in range(1,101):
#     if i&1==0:
#         sum+=i
# print(sum) 
# num=int(input("enter a range"))
# for i in range(1,num):
#     if i&2==0:
#         if i&4==0:
#             print("fizz Buzz")   doubt on this code about this code
#         else:
#             print("fizz")
#     elif i&4==0:
#         print("Buzz")
#     else:
#         print(i)
# num=int(input("enter a range"))
# for i in range(1,num):
#     if i%3==0:
#         if i%5==0:
#             print("fizz Buzz")
#         else:
#             print("fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)
# specific pssword generator
# import random
# password=""
# print("welcome to password generator")
# a=int(input("enter how many letters do you need"))
# b=int(input("enter how many symbols do you need"))
# c=int(input("enter how many numbers do you need"))
# list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','u','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','K','L','M','N','O','P','P','Q','R','S','T','U','V','W','X','Y','Z']
# for i in range(0,a):
#     password+=random.choice(list1)
# list2=['1','2','3','4','5','6','7','8','9','0']
# list3=['!','@','#','$','%','^','&','*','(',')','<','>']
# for i in range(0,b):
#     password+=random.choice(list2)
    
# for i in range(0,c):
#     password+=random.choice(list3)
# print(password)
# hangman game
# import random
# word=input("enter a word to play only enter small only")
# d=len(word)
# print(f"length of the word is {d} so you have {d} choices to enter")
# # guess=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','u','r','s','t','u','v','w','x','y','z']
# count=0
# e=0
# for i in range(0,d):
#     guess=input("enter a word")
#     for s in word:
#         if guess==s:
#             count+=1

#         else:
#             e+=1
# if count==len(word):
#     print("you beat it")
# else:
#     print(f"you lose it better luck next time you gussed correctly{count} you spelt{e} wrong")
# def product_of_numbers(product,*numbers):
#     for i in numbers:
#         product*=i
#     print("product of the numbers",product)

# product_of_numbers(1,1,2,3,4,5)
a=input("enter a word to print")
print(a[-1:-6])
    # print(i)