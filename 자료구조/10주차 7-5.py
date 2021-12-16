class Entry:
    def __init__ (self,key,value):
        self.key = key
        self.value = value
    
    def __str__ (self):
        return str("%s:%s" %(self.key,self.value))

class BinarySearchMap:
    def __init__ (self):
        self.table=[]

    def size(self): 
        return len(self.table)

    def display(self,msg):
        print(msg)
        for entry in self.table:
            print(" ",entry)

    
    def insert(self,key,value):
        for idx in range(len(self.table)):
            if key < str(self.table[idx]):
                self.table.insert(idx,Entry(key,value))
                return
        self.table.append(Entry(key,value))

    def binary_search(self,A,key,low,high):
        while(low<= high):
            middle=(low+high)//2
            if key == A[middle].key:
                return middle
            elif(key > A[middle].key):
                low = middle+1
            else:
                high = middle -1
        return None

    def search(self,key):
        pos = self.binary_search(self.table,key,0,self.size()-1)
        if pos is not None:
            return self.table[pos]
        else:
            return None
    
    def delete(self,key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return

map = BinarySearchMap()						
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