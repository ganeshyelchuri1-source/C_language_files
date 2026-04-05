# a=input("enter a word")
# vowel="aeiouAEIOU"
# v=0
# c=0
# for i in a:
#     if i in vowel:
#         v+=1
# print(f"{v}   and {c}")
# a=input("enter a word")
# for i in  range(0,len(a),2):
#     print(a[i])
# a=input("enter a word")
# str="abcdefghijklmnopqurstuvwxyz"
# str1="ABCDEFGHIJKLMNOPQURSTUVWXYZ"
# up=0
# lo=0
# for i in a:
#     if i in str:
#         up+=1
#     elif i in str1:
#         lo+=1
# print(up)
# print(lo)
# a=input("enter a word")
# vowel="aeiouAEIOU"
# v=0
# c=0
# for i in a:
#     if i in vowel:
#         v+=1
#     else:
#         c+=1
# a=input("enter a word")
# count=0
# for i in  a:
#     if i>='0' and i<='9':
#         count+=1
# print(f"digits {count}")
# a=input("enter a word")
# res=""
# vowel="aeiouAEIOU"
# v=0
# c=0
# for i in a:
#     if i in vowel:
#         res=res+"*"
#     else:
#         res=res+i
# print(res)
# a=input("enter a word")
# vowel="aeiouAEIOU"
# v=0
# c=0
# for i in a:
#     if i in vowel:
#         v+=1
#     else:
#         c+=1
# if v>c:
#     print("more vowels")
# elif c>v:
#     print("more consonants")
# a=input("enter a word")
# res=""
# str="abcdefghijklmnopqurstuvwxyz"
# str1="ABCDEFGHIJKLMNOPQURSTUVWXYZ"
# v=0
# c=0
# for i in a:
#     if i in str:
#         res=res+i
#     elif i in str1:
#         res=res+i
#     else:
#         res+=""
# print(res)
# a=input("enter a word")
# are=""
# for i in a:
#     are=i+are
# print(are)
# a=input("enter a word")
# count=0
# c=len(a)
# for i in a:
#     if i>='a' and i<='z' or i>='A' and i<='Z':
#         count+=1
#     elif i>='0' and i<='9':
#         count+=1
# print(f"{c-count}")
# word=input("enter a word")
# vowel="aeiouAEIOU"
# count=0
# d=len(word)-1
# while d>-1:
#     if word[d] in vowel:
#         count+=1
#     d-=1
# print(f"count is {count}")
# word=input("enter a word that will prints its alphabets until a vowel is found")
# length=len(word)
# vowel="aeiouAEIOU"
# d=0
# while d<length:
#     if word[d]  not in vowel:
#         print(word[d])
#     elif word[d] in vowel:
#         break   
#     d+=1      
# word=input("enter a word that returns no.of spaces in the word")
# d=len(word)
# i=0
# count=0
# while i<d:
#     if word[i]==" " and word[i+1]!=" ":
#         count+=1
#     i+=1
# print(f"{count}")
# word=input("enter a word that returns how many alphabets and numbers are present")
# d=len(word)
# count_letter=0
# count_number=0
# i=0
# while i<d:
#     if ord(word[i])>=67 and ord(word[i])<=90 or ord(word[i])>=97 and ord(word[i])<=123:
#         count_letter+=1
#     elif int(word[i])>=0 and int(word[i])<=9:
#         count_number+=1
#     i+=1
# print(f"l,n{ count_letter , count_number}")
# word=input("enter a word that returns the first upper case letter in the string")
# d=len(word)
# i=0
# while i<d:
#     if ord(word[i])>=67 and ord(word[i])<=90:
#         print(word[i])
#     i+=1
# word=input("enter a word that returns how many special characters are present")
# d=len(word)
# count_special=0
# i=0
# while i<d:
#     if ord(word[i])>=67 and ord(word[i])<=90 or ord(word[i])>=97 and ord(word[i])<=123:
#         pass
#     else:
#         count_special+=1
#     i+=1
# print(f" count is {count_special}")
# word=input("enter a word that prints  characters in the reverse order")
# d=len(word)-1
# i=0
# while d>-1:
#     print(word[d])
#     d-=1
# word=input("enter a word that says that this word contains atleast one vowel or not")
# d=len(word)-1
# str="aeiouAEIOU"
# while d>-1:
#     if word[d] in str:
#         print(word[d])
#         print("it occured ")
#         break
#     d-=1
# word=input("enter a word that returns no.of words in the string")
# d=len(word)
# i=0
# count=0
# while i<d:
#     if word[i]==" " and word[i+1]!=" ":
#         count+=1
#     i+=1
# print(f"{count+1}")
word=input("enter a word  that classify it as vowel,consonant,digit,special character.")
d=len(word)-1
str="aeiouAEIOU"
notstr="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
numstr="0123456789"
v_count=0
con_count=0
num_count=0
special=0
while d>-1:
    if word[d] in str:
        v_count+=1
    elif word[d] in numstr:
        num_count+=1
    elif word[d] in notstr:
        con_count+=1
    else :
        special+=1
    d-=1
print(f"v,con,num,special{v_count,con_count,num_count,special}")
