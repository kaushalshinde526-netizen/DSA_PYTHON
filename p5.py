class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class SingleLinkedList:
    def __init__(self):
        self.head=None


    def insert(self,ele):
        if self.head==None:
            self.head=Node(ele)
        else:
            ptr=self.head
            while ptr.next !=None:
                ptr=ptr.next

            ptr.next=Node(ele)


    def show(self):
        print("HEAD ",end="---> ")

        ptr=self.head

        while ptr !=None:
            print(ptr.data,end="--> ")
            ptr=ptr.next

        print("NULL ")


    def delete(self,ele):

        if self.head.data==ele:
            self.head=self.head.next

        else:
            back=None
            ptr=self.head

            while(ptr!=None) and (ptr.data!=ele):
                back=ptr
                ptr=ptr.next


            if ptr==None:
                print(ele,"not found")

            else:
                back.next=ptr.next
                print(ele,"deleted")



print("Hi")

s=SingleLinkedList()


while True:

    op=int(input("1 add , 2 show , 3 remove and 4 exit "))


    if op==1:
        ele=input("enter first ele ")
        s.insert(ele)


    elif op==2:
        s.show()


    elif op==3:
        ele=input("enter element to remove ")
        s.delete(ele)


    elif op==4:
        print("Bye")
        break


    else:
        print("Invalid input")