class DNode:
    def __init__ (self,elem,prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next

class myDoubleLinkedListQueue:
    def __init__ (self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    
    def clear(self):
        self.front = self.rear = None
    
    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.next
            count+=1
        return count
    
    def display(self,msg='myDoubleLinkedListQueue: '):
        print(msg,end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.next
        print()

    def equeue(self,item):
        node = DNode(item,self.rear,None)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data

# test code: DO NOT MODIFY
d = myDoubleLinkedListQueue()
d.equeue(10); d.equeue(20); d.equeue(30); d.equeue(50)
d.equeue(60); d.equeue(70); d.equeue(80); d.equeue(90)

d.dequeue(); d.dequeue(); d.dequeue()

print("queue size: ", d.size())
d.display()