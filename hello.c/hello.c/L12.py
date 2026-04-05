class my_list:
    def __init__(self):
        self.l=[0,0,0,0,0]
        self.count=0
    def my_append(self,value):
        self.value=value
        self.l[self.count]=self.value
        self.count=self.count+1
        
    def print_list(self):
        print("[")
        for i in range(self.count):
            print(self.l[i],end=" ")
        print("]",end="") 
    def pop(self):
        name=self.l[self.count-1]
        self.count=self.count-1
        return name  #in the  list enter a element at certain position,,same as delete
    def changevalue(self,value,p):
        self.value=value
        self.p=p
        self.l[self.p-1]=self.value
    def deleteelement(self,value):
        for i in range(0,self.count):
            if self.l[i]==value:
                for d in range(i,self.count-1):
                    self.l[d]=self.l[d+1]
                # self.count-=1
            else:
                print("not there")
    # def deleteelement(self,value):
    #     self.value=value
    #     for i in range(0,self.count+1):
    #         if self.l[i]==self.value:
    #             a=i
    #             break
    #         while a<=self.count-1:
    #             self.l[a]=self.l[a+1]
    #             a+=1
    #         self.count-=1
    # def delete_index_element(self,index):
    #     # self.index=index
    #     if index<=self.count:
    #         for i in range(index,self.count):
    #             self.l[i]=self.l[i+1]
    #             # self.index+=1
    #         self.count-=1
    #     else:
    #         print("not possible")
    # def udate(self,value,index):
    #     self.l[index]=value

    # def insertposition(self,pos):
    #     p=int(input("enter a number"))
    #     self.count+=1
    #     for i in range(self.count,p):
    #         self.l[count-1]=self.l[]
    #     name=self.l[count-1]
l1= my_list()
l1.my_append(4)
l1.my_append(7)
l1.my_append(3)
l1.my_append(2)
l1.my_append(1)
# print(l1.pop())
# l1.replace(40,3)
# l1.insertposition(3)
l1.deleteelement(3)
# l1.delete_index_element(2)
l1.print_list()