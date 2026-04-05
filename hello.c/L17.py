# list comprehension

# l=[i for i in range(1,11)]
# print(l)
# l1=[i*i for i in range(1,11)]
# print(l1)
# l2=[chr(i) for i in range(65,97)]
# print(l2)
# s="sai university"
# l3=[i for i in s]
# print(l3)
# l4=[i for i in range(1,20) if i%2==0 ]
# print(l4)
# find for else part 
# [value_if_true if condition else value_if_false for item in iterable]
# l4 = [i if i % 2 == 0 else "not an even integer" for i in range(1, 20)]
# print(l4)
#dictionary compression
# d={i:i*i for i in range(1,9)}
# print(d)
# d1={chr(i) :i for i in range(65,75)}
# print(d1)
# s='ABCDEFGHIJKL'
# d2={ord(i):i for i in s if i not in "AEIO"}
# print(d2)
#tupple comprehension
# t=(12,4,5,6,6)#tupple is immutable(does not  be updated/can not be changed) 
# print(type(t))
# print(t)
# t[1]=3
# print(t)#'tuple' object does not support item assignment
# t1=t[1:4]
# print(t1)
# t2=t[::-1]
# print(t2)
# l=list(t)#type casting
# print(l)
# print(type(l))
# l[0]=13
# tu=tuple(l)
# print(tu)

#difference between short and shorted
# l=[1,5,6,7,83,5]
# l1=l.sort()
# print(l)
# l2=sorted(l)
# print(l)
# print("l",l)
# print("l1",l1)
# print("l2",l2)
# l=["red","orange","brown"]
# l1=l#we are pointing the elements
# l1.append("violet")
# print(l)
# print(l1)
# in this place we are coping the elements
# l1=l[:]
# l1.append("blue")
# print(l)
# print(l1)

#sets
# s=set()
# s1={0}#all are absent menas dict if anyone present means set
# print(type(s))
# print(type(s1))
# print(s)
# l=[4,5,2,6,7,1,0]
# for i in l:
#     s.add(i)
# print(s)
# l=list(s)
# print(l)
# s.remove(1)
# print(s)
# s.pop()
# print(s)
#hw 
