# # l=[1,2,3,4,5]
# # print(l)
# # print(type(l))
# # l.append(20)
# # print(l)
# # l.insert(3,45)
# # print(l)
# # # print("started slicing")
# # # print()
# # l.pop()
# # print(l)
# list=[22,3,33,22,1,2,3,4,6]    #removes first element of which you entered and duplicates remains same
# list.remove(22)
# print(list)
# list.reverse()
# print(list)
# print(list.index(3))   #what is the error
#   #says thaat 2 is present at which index     else  shows value error
# print(list.count(3))
# lists=["n__ame",23,"scds",[1,2,2,23,4,5,6]]
# print(lists[0])
# print(type(lists[1]))   #here n__me is subdivided into string level it is only possible where there is only a string  and the elements belongs to their respected classes
# # for i in range(len(lists[0])):       #how do len   fn function,
# #     print(lists[0][i],end='')
# for i in range(0,len(lists)):
#     print(lists[i],sep="")
# def len1(n):
#     if isinstance(n,str):
#         count=0
#         for i in n:
#             count+=1
#         return f"length of the list is {count}"
#     elif isinstance(n,list):#what is work of isinstance
#         count1=0
#         for i in n:
#             count1+=1

#         return f"lentgh of the list is {count1}"
#     else:
#         return "wrong data structure"
# print(len1("my_name"))
# print(len1([1,2,3,4,6]))
# print(len1(234))
# l1=input("enter a number")----------------
# # list=[]
# list=l1.split(" ")
# print(list)
# for i in list:
#     i=int(i) # how to do this thing is this work
# # num=list[0]
# print(list)
# print(type(list[0]))

# for i in range(0,len(list)):
#     num=list[i]# is there any type casting thing to aoid comparing problem means type error
#     for j in range(i+1,len(list)):
#         if num>=list[j]:
#             temp=num
#             num=j
#             j=temp
# creating a list from a string and accesing the elements
# print(list[-2])
# i=input("enter a  number")
# list=i.split()
# print(list)
# sublist=[(list[0][a])for a in range(0,len(list[0]))]
# print(sublist)
# finding max and min in the list
# list=[6,3,4,2,8,5,2,1,9]
# min=max=list[0]
# for i in range(0,len(list)):
#     if min>list[i]:
#         min=list[i]
#     if max<list[i]:
#         max=list[i]
# print(max)
# print(min) 
# converting the list from one data type to another
# num=input("enter an number").split(" ")
# print(num)
# num_mod=list(map(int, num))
# print(num_mod)
