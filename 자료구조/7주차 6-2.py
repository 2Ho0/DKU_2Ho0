class Node:
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link
    
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def clear(self):
        self.head = None
    
    def size(self):
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count+=1
        return count
    
    def display(self, msg="LinkedStack: "):
        print(msg,end='')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

    def getNode(self,pos):
        if pos < 0:
            return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos-=1
        return node

    def getEntry(self,pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self,pos,elem):
        node = self.getNode(pos)
        if node != None:
            node.data = elem
    
    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return node

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem,self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
    
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

    def merge(self,elem):
        before = self.getNode(self.size()-1)
        
        before.link = elem.head

class myLinkedListQueue:
    def __init__(self):
        self.tail = None
        self.head = None
    def isEmpty(self):
        return self.tail == None
    def clear(self):
        self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def equeue(self,item):
        node = Node(item,None)
        if self.isEmpty():
            self.head = node
            self.tail = node
            self.head.link = self.tail
        else:
            self.tail.link=node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            node = self.head
            value = node.data
            self.head = self.head.link
            del node
            return value
    def size(self):
        #덱용
        # if self.isEmpty():
        #     return 0
        # else:
        #     count = 1
        #     node = self.tail.link
        #     while not node == self.tail:
        #         node = node.link
        #         count +=1
        #     return count
        #큐용
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count+=1
        return count
    def display(self,msg='myLinkedListQueue: '):
        #덱용
        # print(msg,end='')
        # if not self.isEmpty():
        #     node = self.tail.link
        #     while not node == self.tail:
        #         print(node.data, end=' ')
        #         node = node.link
        #     print(node.data,end=' ')
        # print()
        #큐용
        print(msg,end='')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

# s = LinkedList()
# t = LinkedList()


# s.display('단순열결리스트로 구현한 리스트(초기 상태): ')
# s.insert(0,10)
# s.insert(0,20)
# s.insert(1,30)
# s.insert(s.size(),40)
# s.insert(2,50)
# t.insert(0,100)
# s.merge(t)


# s.display('단순열결리스트로 구현한 리스트(삽입 x5): ')
# s.replace(2,90)
# s.display('단순열결리스트로 구현한 리스트(교체 x1): ')
# s.delete(2)
# s.delete(s.size()-1)
# s.delete(0)
# s.display('단순열결리스트로 구현한 리스트(삭제 x3): ')
# s.clear()
# s.display('단순열결리스트로 구현한 리스트(정리 후): ')

s = myLinkedListQueue()
s.equeue(10); s.equeue(20); s.equeue(30); s.equeue(50)
s.equeue(60); s.equeue(70); s.equeue(80); s.equeue(90)

s.dequeue(); s.dequeue(); s.dequeue()

print("queue size: ", s.size())
s.display()
