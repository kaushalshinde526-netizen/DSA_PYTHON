#QUEUE (WAPPPMDPOOP FOR LINEAR DS: QUEUE-->FIFO)
class Queue:
    def __init__(self):
        self.data=[]
    def enq(self,ele):
        self.data.append(ele)
        print(ele,"Is insert into the queue")
        self.data.sort(reverse=True)
    def deq(self):
        if len(self.data)==0:
            return " queue is empty "
        else:
            return self.data.pop(0)
    def show(self):
        print(self.data)
print("Hi")
q=Queue()
while True:
    op=int(input("1 enq , 2 deq , 3 show and 4 exit "))
    if op==1:
        ele=input("enter element ")
    elif op==2:
        print(q.deq())
    elif op==3:
        q.show()
    elif op==4:
        print("Bye")
        break
    else:
        print("Invalid input")
    