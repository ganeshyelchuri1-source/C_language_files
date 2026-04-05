a=input("enter a number")
lis=a.split(' ')
l=list(map(int, lis))
extra=[]
print(l)
for i in range(0,len(l)):
    min=l[i]
    for j in range(i+1,len(l)):
        if min>l[j]:
            temp=min
            min=l[j]
            l[j]=temp
    extra.append(min)

print(extra)
print(extra[len(extra)-2])