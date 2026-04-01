# list=[1,2,4,6,2,1]
# output=""
# count=0
# num=int(input("enter the target sum"))
# for i in list:
#         for j in range(i+1,len(list)):
#             if i+list[j]==num:
#                   count+=1

# print(count)
# l=[1,2,4,6,2,1]
# count=0
# s=int(input("enter  a number"))
# res=[]
# for i in l:
#     if i in l:
#         if i+j==s:
#             count+=1
# print(count)
#file handeling
# with open("text.txt","r") as f:
#     data = f.read()
# print(data)
# print(type(data))
# count=1
# for i in data:
# #     if i !=" " and i!='\n':
# #         count+=1
# # print(count+1)
#     if i =='\n':
#         count+=1
# print(count)
# with open("text.txt","r") as f:
#     #data=f.readline()  #will gives the first line of the file
#     data=f.readlines()
# print(data)
# print(data[0])
# text_file="text.txt"
# with open(text_file,"w") as f:
#     f.write("my name is y \n i completed my education")
# with open("text.txt","a") as f:
#     f.write("nothing")
#     f.write("\ni am sleeping \n")
def say(data):
    for i in data:
        if i==something:
            i=nothing
    return data
with open("text.txt","r") as f:
    data=f.read()
with open("5.py","w") as f:
    f.write(data)
with open("5.py","a") as f:
    f.write(say(data))