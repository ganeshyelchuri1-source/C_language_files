# d1={"a":["d","e"],"b":["e","c"],"c":["b"],"d":["a","e"],"e":["a","b","d"]}
# # # print(d1["a"])
# # # print(d1["b"])
# b=input("enter a nodes")
# c=input(" enter a value")
# if b in d1.keys():
#     if c in d1[b]:#d1[n1] is a list for char n1
#         print("yes are connected")
#     else:
#         print("b is there but they are not connected")
    # else:
    #     print("there not present and not connected")
# # ae=input("enter a value")
# # be=input("enter anoter value")
# # # c=input("enter third node")

# # if ae in d1[a] and be in d1[a]:
# #     print("yes")
# # elif ae in d1[b] and be in d1[b]:
# #     print("yes")
# # elif ae in d1[c] and be in d1[c]:
# #     print("yes")
# # elif ae in d1[d] and be in d1[d]:
# #     print("yes")
# # elif ae in d1[e] and be in d1[e]:
# #     print("yes")
# # else:
# #     print("not there")
# # if n1 and n2 and n3 in keys():
# #     if n2 in d1[n1]:
# #         print("they are connected")
# for i,j in d1.items():
#     print(i,j)
# print(get(a))
# def separate(str):
#     list=str.split("")
#     print(list)
# str=input("enter a string")
# separate(str)
# def seperate(s):
#     d1={}
#     for i in s:
#         if i not in d1.keys():
#             d1[i]=1
#         else:
#             d1[i]+=1
#     print(d1)
# seperate("carootoonnnn")
# def seperate(s):
#     d1={}
#     word=""
#     final=[]
#     for i in s:
#         if i not in d1.keys():
#             d1[i]=1
#         else:
#             d1[i]+=1
#     for i in d1.keys():
#         for j in range(d1[i]):
#             word=word+i
#         final.append(word) # how did this . operator work
#         word=""
#     return final
#     print(d1)
# print(seperate("carootoonnnn"))
# def movedups(s):
#     d1={}
#     s1=""
#     s2=""
#     for i in s:
#         if i not in d1.keys():
#             d1[i]=1
#             s1=s1+i
#         else:
#             s2=s2+i
#     return s1+" "+s2
# print(movedups("aabbbcccc"))