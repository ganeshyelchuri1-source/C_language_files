# s="table tennis"
# for i in range(0,25):
#     try:
#         print(s[i])
#     except IndexError:
#         print("Avoiding Error")
# str="table tennis"
# for i in str:
#     print(i)
# when range is grater than required this will print
#syntax of the function
# if we dont return anything it will return none
# def great():
#     print("hello world")
#     # return "tennis"
#     #  if you written pass prits return
# print(great())
# def change(x):
#     x=x+1
#     return x
# x=4
# print(x)
# x=change(x)
# print(x) #call by referance
# def change(x):
#     x=x+1
#     return x
    
# x=4
# print(x)
# print(change(x))
# print(x) #should know
# def change(x):
#     def g(x):
#         x="table tennis"
#         print(x)
#     g(x)
#     x=x+1
#     return x
# x=4
# print(x)
# print(change(x))

# print(x)
# print(x)
# def say(arr):
#     count=0
#     for i in range(0,150):
   
#         try: if arr[i]=='a' or arr[i]=='e' or arr[i]=='i' or arr[i]=='o' or arr[i]=='u' or arr[i]=='A' or arr[i]=='E' or arr[i]=='I' or arr[i]=='O' or arr[i]=='U':
#             count=count+1
#             print(i)
#         except IndexError:
#             print("")
# i=input("enter a word")

# def say(str):
#     vo=0
#     co=0
#     vowels='aeiouAEIOU'
#     for i in str:
#         if i in vowels:
#             vo+=1
#         else:
#             co+=1
#     print(co)
#     print(vo)

# str=input("enter num")
# say(str)