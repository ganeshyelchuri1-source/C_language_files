# def year_check(word):
#     year=word
#     if year>=1600 and year<=9999:
#         if year%400==0 and year%100==0 or year%4==0:
#             print("it is an leap year")
#             return True
#     else:
#         return False

# word=int(input("enter a year that says that wheather the year is leap year or not"))
# print(year_check(word))
# def voco_check(word):
#     str="aeiouAEIOU"
#     vo=co=0
#     d=len(word)-1
#     while d>-1:
#         if word[d] in str:
#             vo+=1
#         else:
#             co+=1
#         d-=1
#     print(f"v={vo},c={co}")
# word=input("enter a string that returns no.of vowels and consonents")
# voco_check(word)

# def table(a):
#     for i in range(1,11):
#         print(f"{a} X {i}={a*i}")
# a=int(input("enter a number"))
# table(a)

# def square(a):
#     print(a*a)
# a=int(input("enter a number"))
# square(a)

