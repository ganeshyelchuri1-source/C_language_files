# # l = [a for a in range(100)]
# # print(l)
# # l = []
# # for ch in range(12):
# #     l.append(ch)
# # print(l)
# # l = [10,20,30,40,50]
# # print(l[2]) # 30
# # print(l[0]) # 10
# # print(l[-2]) # 40
# # print(l[400]) # Index Error
# # l = [ch for ch in range(20,0,-2)]
# # print(l)
# # l[1] = 888
# # print(l)
# # l = [10,20,10,40,50,10,70,80,90,100]
# # print(l.index(10))
# # print(l.count(10))
# # list=["orange","banana","apple"]
# # s=",".join(list)
# # print(s)
# # print(type(s))
# # list="btmti2507980"
# # print(list.isalnum())
# name=input("enter a number")
# str=""
# num=0
# str=""
# output=""
# for i in name:
#     if i.isalpha():
#         str=i
#     if i.isdigit():
#         for s in range(0,int(i)):
#             output+=str
# print(output)


a=int(input("enter a number"))
for i in range(0,a):
    try :
        if i<5:
            print(i)
    except IndexError:
        print("not axcess")