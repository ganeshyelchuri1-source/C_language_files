# # code that updation is possible without using any type of function means not very efficient
# code that updation is possible with using function means  very efficient
class matrix:
    def __init__(name):
        name.l=[0,0,0,0,0,0,0,0]
        name.count=0
    def append_it(name,element):
        name.element= element
        name.l[name.count]=name.element
        name.count+=1
    def print_the_list(name):
        try:
            print("[",end="")
            for i in range(0,name.count):
                print(name.l[i],end=" ")
            print("]",end="")
        except IndexError:
            print("you are inserting but there is no space")
    def pop(name):
        # name.value=value
        # if value==None:
            print(name.l[name.count-1])
            name.count-=1
        # else:
        #     matrix(element)
        #     for i in range(0,name.count):
        #         if i==name.value:
        #             element=name.value
        #     name.l[element]=None
    def remove_at_element(name,value):
        name.value=value
        element=None
        name.element=element
    
        for i in range(0,name.count):
            if name.l[i]==name.value:
                name.element=i
        name.l[name.element]=""   #when i write the None at here i think that it work like null?
    def remove_index(name,index):
        name.index=index
        
        
d1=matrix()
d1.append_it(4)
d1.append_it(6)
d1.append_it(7)
d1.append_it(8)
d1.append_it(9)
d1.append_it(10)
d1.append_it(11)
d1.append_it(12)
d1.pop()
d1.print_the_list()
# d1.remove_at_element(1)
# d1.print_the_list()
d1.remove_index(3)
d1.print_the_list()






















#in the dictionary
# dictionary={}
# s1=input("enter a word that will convert into the dictionary")
# for i in s1:
#     if i not in dictionary:
#         dictionary[i]=1
#     else:
#         dictionary[i]+=1
# print(dictionary)
# dictionary={}
# s1=input("enter a word that will present its reputaions in the form of dictionary")
# s3=""
# s4=""
# for i in s1:
#     if i not in dictionary:
#         dictionary[i]=1
#         s3+=i
#     else:
#         dictionary[i]+=1
#         s4+=i
# print(dictionary)
# print(f"its reputations in the string form is{s3+""+s4}")