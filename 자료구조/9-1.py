class OrderedListSet:
    def __init__(self):
        self.items=[]
    
    def __eq__(self, setB):
        if self.size()!=setB.size():
            return False
        for idx in range(len(self.items)):
            if self.items[idx]!= setB.items[idx]:
                return False
        return True

    def size(self):
        return len(self.items)

    def display(self,msg):
        print(msg, self.items)

    def contains(self,item):
        for i in range(len(self.items)):
            if self.items[i]==item:
                return True
        return False

    def insert(self,elem):
        if elem in self.items: return
        for idx in range(len(self.items)):
            if elem < self.items[idx]:
                self.items.insert(idx,elem)
                return
        self.items.append(elem)

    def delete(self,elem):
        result = self.contains(elem)
        if result == True:
            self.items.pop(self.items.index(elem))

    def union(self,setB):
        setC = OrderedListSet()
        setC.items = list(self.items)
        for elem in setB.items:
            result = self.contains(elem)
            if result == False:
                setC.insert(elem)
        return setC

    def intersect(self,setB):
        setC = OrderedListSet()
        for elem in setB.items:
            result = self.contains(elem)
            if result == True:
                setC.insert(elem)
        return setC

    def difference(self,setB):
        setC=OrderedListSet()
        for elem in self.items:
            if elem not in setB.items:
                setC.insert(elem)
        return setC
    # def __sub__(self,setB):
    #     setC = OrderedListSet()
    #     for elem in self.items:
    #         result = setB.contains(elem)
    #         if result == False:
    #             setC.items.append(elem)
    #     return setC

    def isSubsetOf(self, setB):
        for elem in self.items:
            result = setB.contains(elem)
            if result == False:
                return print("setA는 setB의 부분 집합이 아닙니다.")
        return print("setA는 setB의 부분 집합입니다.")


setA = OrderedListSet()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = OrderedListSet()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A – B:')