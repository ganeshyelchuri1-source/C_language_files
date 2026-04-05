health_condition=input("enter your health condition")
age=int(input("enter your age"))
gender=int(input("enter your gender"))
location=input("enter your place that is rural or urban")
premium=0
maximum_policy=0
if age>=18 and age<=60:
    if location=="city":
        if health_condition=="excellent":
            if gender=="male":
                print("eligible for insurance")
                premium=4000
                maximum_policy=200000
print(premium)
print(maximum_policy)
binary_digit=input("enter the binary digit value")
count=0
int_digit=0
for i in range(len(binary_digit)-1,0,-1):
    
    int_digit+=i*(2**count)
    count+=1
print(int_digit)
def checking(output,input):
    if output==input:
        print("it is an amstrong number")
    else:
        print("it is not a amstrong number")
number=int(input("enter a number says that wheather it is amstrong or not"))
a=number
input=a
count=0
output=0
while a!=0:
    count+=1
    a=a//10
while number!=0:
    b=number%10
    output+=b**count
    number//=10
checking(output,input)
def roots(a,b,c):
    r1=(-b+(b*b-(4*a*c))**1/2)/2*a
    r2=(-b-(b*b-(4*a*c))**1/2)/2*a
    if r1>0:
        print(round(r1))
    if r2>0:
        print(round(r2))
    else:
        print(r1,r2)

d=input("enter a b c values")
a,b,c=d.split(" ")
a=int(a)
b=int(b)
c=int(c)
roots(a,b,c)
def checking(count):
    if count==0:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
word=input("enter a number that says thar wheather it is palindrome or not")
j=len(word)
i=int(0)
for i in range(0,j):
    if word[i]!=word[j-1]:
        count=1
        break
    j-=1
checking(count)
def shift(str,acount):
    i=0
    j=0

    for i in range(acount,len(str)):
        print(str[i],end="",sep="")
        i+=1
    for j in range(0,acount):
        print(str[j],end="",sep="")
        j+=1
str=input("enter a  word")
acount=int(input("enter a value so that it get changed shifted"))
shift(str,acount)
# "or"1 in 2
def shift(s,acount=0,ccount=0):
    final=s
    len_str=len(s)
    if(ccount>0):
        final=s[len_str-ccount::]+s[:len_str-ccount:]
    if(acount>0):
        final=final[acount::]+final[:acount:]
    return final
    
acount=int(input("enter the acount : "))
ccount=int(input("enter the ccount : "))
name=input("enter the string")
print(shift(name,acount=acount,ccount=ccount)) 
class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def addition(self,others):
        x=self.x+others.x
        y=self.y+others.y
        z=self.z+others.z
        return vector(x,y,z)
    def subtraction(self,others):
        x=self.x-others.x
        y=self.y-others.y
        z=self.z-others.z
        return vector(x,y,z)
    def __str__(self):
        return f"{self.x}i+{self.y}j+{self.z}z"
    def dot_product(self,others):
        
        c1=self.x*others.x+self.y*others.y+self.z*others.z
        return c1
    def sclar_multiplication(self,k):
        self.k=k
        c1=self.k*self.x+self.k*self.y+self.k*self.z
        return c1
c1=vector(1,2,3)
print(c1)
c2=vector(3,2,1)
print(c2)
c3=c1.addition(c2)
print(c3)
c3=c1.subtraction(c2)
print(c3)
c3=c1.dot_product(c2)
print(c3)
c3=c1.sclar_multiplication(3)
print(c3)
def largest(k,size):
    if k>size:
        print("k is out of range")
    else:
        print(list[k-1])
size=int(input("enter a size"))
list=[]
for i in range(0,size):
    value=int(input("enter the element"))
    list.append(value)
list.sort()
list.reverse()
k=int(input("which largest element "))
largest(k,size)
def delvowels(word):
    vowel_set="aeiouAEIOU"
    new=""
    for i in word:
        if i in vowel_set:
            new+=""
        else:
            new+=i
    print(new)
word=input("enter a word")
delvowels(word)
def moveDups(s):
    seen = ""
    dup = ""

    for c in s:
        if c not in seen:
            seen += c
        else:
            dup += c
    print(seen + "_" + dup)
str=input("enter a word for duplicates")
moveDups(str)
def extractDup(lst):
    dup = []
    for i in lst:
        if lst.count(i) > 1 and i not in dup:
            dup.append(i)
    print(dup)
a=input("enter the elements by se-perating with \"  \"")
list=a.split(" ")
extractDup(list)
def distChar(s1, s2):
    res = ""
    for c in s1:
        if c not in s2 and c not in res:
            res += c

    for c in s2:
        if c not in s1 and c not in res:
            res += c

    print(res)
word=input("enter the string : ")
index1=0
biglen=0
bigpal=""
for i in word:
    index2=len(word)
    for j in word[::-1]:
        if i==j:
            s=word[index1:index2]
            if s==s[::-1]:
                if(len(s)>=len(bigpal)):
                    bigpal=""+s
                break
        index2-=1
    index1+=1
print(bigpal)

w1=input("enter a word")
w2=input("enter word2")
(distChar(w1,w2))
def mat_mul(A, B):
    n = len(A)
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
A = [[4,5,6],[1,2,3][1,1,1]]
B = [[10,3,9],[1,1,0],[0,0,0]]
print(mat_mul(A,B))
def minOp(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])
    return dp[m][n]
str1=input("enter a string")
str2=input("enter another string")
print(minOp(str1,str2))