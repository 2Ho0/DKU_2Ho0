class Node:
    def __init__(self,elem,link=None):
        self.data = elem
        self.link = link

class Entry:
    def __init__ (self,key,value):
        self.key = key
        self.value = value
    
    def __str__ (self):
        return str("%s:%s" %(self.key,self.value))

class LinearProbingHashMap:
    def __init__ (self,M):
        self.table = [None]*M
        self.M = M
    def hashFn(self,key):
        sum = 0
        for c in key:
            sum = sum+ ord(c)
        return sum% self.M
    def insert(self,key,value):
        idx = self.hashFn(key)
        for i in range(len(self.table)):
            if self.table[idx]==None:
                self.table[idx] = Node(Entry(key,value),self.table[idx])
                break
            else:
                if idx == len(self.table)-1:
                    idx=0
                else:
                    idx+=1    

    def search(self,key):
        idx = self.hashFn(key)
        for i in range(len(self.table)):
            if idx == len(self.table)-1:
                idx=0
            node = self.table[idx]
            if node == None:            
                idx+=1
            else:
                if node.data.key == key:
                    return node.data
                else:
                    idx+=1
    def isValid(self,node):
        if node==None:
            return True 
        else:
            return False

    def delete(self,key):
        idx = self.hashFn(key)
        before = None
        for i in range(len(self.table)):
            if idx == len(self.table)-1:
                idx=0
            node = self.table[idx]
            if self.isValid(node):
                if idx == len(self.table)-1:
                    idx=0
                else:
                    idx+=1
            else:
                if node.data.key == key:
                    if before == None:
                        self.table[idx] = node.link
                    else:
                        before.link = node.link
                    return
                else:
                    if idx == len(self.table)-1:
                        idx=0
                    else:
                        idx+=1
            
    def display(self,msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] -> "%idx, end="")
                while node is not None:
                    print(node.data, end=' -> ')
                    node = node.link
                print()

hashmap_size = 8
map = LinearProbingHashMap(hashmap_size)							
map.insert('data', '자료')					
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')	
map.display("나의 단어장: ")			

print("탐색:game --> ", map.search('game'))	
print("탐색:over --> ", map.search('over'))
print("탐색:data --> ", map.search('data'))

map.delete('game')						
map.display("나의 단어장: ")