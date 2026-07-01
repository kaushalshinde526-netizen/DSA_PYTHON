#WAPMDPOOP FOR LINER DATA STRUCTURE : STACK-->LIFO/FILO 
class Stack:
    def __init__(self):
        self.data=[]
    def push(self,ele):
        self.data.append(ele)
        print(ele," is push on stack")
    def pop(self):
        if len(self.data)==0:
            return "stack is empty"
        else:
            return self.data.pop()
    def show(self):
        print(self.data)
s=Stack()
print("Hi")
while True:
    op=int(input("1 push ,2 pop , 3 show and 4 exit "))
    if op==1:
        ele=int(input("enter integer "))
        s.push(ele)
    elif op == 2:
        print(s.pop())
    elif op== 3:
        s.show()
    elif op == 4:
        print("Bye")
        break
    else:
        print("invalid input")
