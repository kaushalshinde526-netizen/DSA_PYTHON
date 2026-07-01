#DSA-->Data Strute And Algorithms
#wamdoop for DSA  stack
class Stack:
    def __init__(self):
        self.data=[]
    def push(self,ele):
        self.data.append(ele)
    def pop(self):
        if len(self.data)==0:
            return "stack is empty"
        else:
            return self.data.pop()
    def show(self):
        print(self.data)

s=Stack()
while True:
    op=int(input("1 push,2 pop,3 show and 4 exit "))
    if op==1:
        ele=input("enter ele ")
        s.push(ele)
    elif op==3:
        s.show()
    elif op==4:
        break
    else:
        print("invalid operation")