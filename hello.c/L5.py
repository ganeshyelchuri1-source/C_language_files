# for i in range (0, 6):
#     print(i, end = " ")
# for i in range (65,91):
#     print(chr(i), end = " ")
# s1 = "Sai University"
# s2 = "SCDS"
# s3 = s1 + s2 #how this + is working (Objected Oriented Programming Class concept)

# print(s3)

# s4 = "Vaibhav "
# print(f"My name is "+s4+"I am student of "+s1)
# a = int(input("Enter the range : "))
# for i in range (0, a , 2): # ( Start , End , Number of Steps)
#     print(i, end = " ")
# for i in range (0,7):
#     print(s1[i], end = " ")

# s1 = "Sai University"
# for a in s1:
#     print(a, end = "")
# a = int(input("Enter the range : "))

# for i in range (0 , a):
#     if i % 2 == 0 or i % 3 == 0:
#         print(i, end = " ")
# a = int(input("Enter the range : "))

# for i in range (0 , a):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i, end = " ")
# s = "Sai University"
# v = 0
# c = 0
# for i in range (0 , 14 , 1):
#     if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
#         v+=1
#     elif s[i] != " ":
#         c+=1
# print(f"Count of Vowels in the string {s} is {v}")
# print(f"Count of consonants in the string {s} is {c}")
# s1 = "Sai University"
# for i in range (13, -1, -1):
#     print(s1[i], end = "")
s = "Sai University"
for i in range (0, 14, 3):
    print(s[i], end = " - ") 
    print(ord(s[i]), end = "    ") # ord(string) = ASCII Values