# def minop(str1,str2,a,b):
#     count=0
#     output=""
#     if a==b:
#         for i in str1:
#             for j in str2:
#                 if i != j:
#                     count += 1         
#                     pass
#                 else:
#                     output+=j
#                 count+=1
#                 num=count/a

#         print(num)
#         print(output)
#     elif a<b:

#         for i in str1:
#             for j in str2:
#                 if i==j:
#                     output+=i
#                 else:
#                     output+=j
#             count+=1
#         print(count)
#         print(output)
#     elif a>b:
#         num=""
#         for d in range(0,len(b)):
#             num+=d
#         for i in num:
#             for j in str2:
#                 if i==j:
#                     output+=j
#                     pass
#                 else:
#                     output+=j
#                 count+=1
#         a=output
#         print(output)
#     return count
#     # else:
#     #     for i in str1:
#     #         for i in str2:
#     #             if i==j:
#     #                 pass
#     #             elif 
#     #             elif i!=j:
# str1=input("enter a string")
# str2=input('enter second string')
# a=len(str1)
# b=len(str2)
# print(minop(str1,str2,a,b))
# def reversing(a):
#     word=a
#     count=0
#     i=0
#     l=len(word)-1
#     while i<l:
#         temp=word[i]
#         word[i]=word[l]
#         word[l]=temp
#         i+=1
#         l-=1
#     print(word)
# word=input("enter a name to check that is palindrome or not")
# reversing(word)
# def palindrome(a):
#     count=0
#     i=0
#     j=len(a)-1
#     while a[i]!=a[j]:
#         count=1
#         break
#     if count==1:
#         return "no"
#     elif count==0:
#         return "yes"
# a=input("enter a word")
# print(palindrome(a))
# def firstword(word):
#     count=""
#     for i in range(0,len(word)):
#         if i!=" " and i-1!=" ":
#             count+=i-1
#     print(count)
# word=input("enter a string")
# firstword(word)
# name=input("enter a number")
# di={}
# o=""
# oi=""
# for i in name:
#     if i not in di.keys():
#         di[i]=1
#         o+=i
#     else:
#         di[i]+=1
#         oi+=i
# print(di)
# print(o+" "+oi)
# a=input("entera  word")
# d=[]
# word=""
# di={}
# for i in a:
#     if i not in di.keys():
#         di[i]=1
#     else:
#         di[i]+=1
#     # print(di)
# for j in di.keys():
#     for l in range(di[j]):
#         word+=j
#     d.append(word)
#     word=""
# print(d)
# s1 = input("Enter a string : ") #Input = aabbbcccdddd
# d2 = {}
# least_occured = s1[0]
# most_occured = s1[0]
# for i in s1:
#     if i not in d2.keys():
#         d2[i] = 1
#     else:
#         d2[i] += 1
#     if d2[most_occured] < d2[i]:
#         most_occured = i
#     if d2[least_occured] > d2[i]:
#         least_occured = i

# print(f"Most occurred is : {most_occured}")
# print(f"Least occurred is : {least_occured}")
# num=input("enter a word")
# s={}
# for i in num:
#     if i not in s.keys():
#         s[i]=1
#     else:
#         s[i]+=1
# min=num[0]
# max=num[0]
# for i in range(0,len(num)):
#     if s[min]>s[num[i]]:
#         min=num[i]
#     if s[max]<s[num[i]]:
#         max=num[i]
# print(max)
# print(min)
# def change(sr1,st2):
#     count=-1
#     for i in range(len(sr1)):
#         if sr1[i] in st2:
#             count=i
#     return count


# print(change("tiger","integer")
# def call(s1,s2):
#     i=0
#     j=0
#     count=0
#     while i<len(s1) and j<len(s2):
#         if s1[i]==s2[j]:
#             i+=1
#             j+=1
#         else:
#             if i+1<len(s1) and s1[i+1]==s2[j]:
#                 count+=1
#                 i+=1
#             elif j+1<len(s2) and s2[j+1]==s1[i]:
#                 count+=1
#                 j+=1
#             else:
#                 count+=1
#                 i+=1
#                 j+=1
#     count+=(len(s1)-i)
#     count+=(len(s2)-j)
#     print(count)
# s1=input("entera  string")
# s2=input("entera string")
# call(s1,s2)
def call(s1,s2):
    i=0
    j=0
    count=0
    while i<len(s1) and j<len(s2):
        if s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            if i+1<len(s1) and s1[i+1]==s2[j]:
                count+=1
                i+=1
            elif j+1<len(s2) and s2[j+1]==s1[i]:
                count+=1
                j+=1
            else:
                count+=1
                i+=1
                j+=1
    count+=(len(s1)-i)
    count+=(len(s2)-j)
    print(count)
s1=input("enter a string")
s2=input("enter another string")
call(s1,s2)