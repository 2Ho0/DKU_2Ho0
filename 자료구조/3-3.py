class Set:
    def __init__(self):
        self.items=[]

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
        result = self.contains(elem)
        if result == False:
            self.items.append(elem)

    def delete(self,elem):
        result = self.contains(elem)
        if result == True:
            self.items.pop(self.items.index(elem))

    def union(self,setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            result = self.contains(elem)
            if result == False:
                setC.items.append(elem)
        return setC

    def intersect(self,setB):
        setC = Set()
        for elem in setB.items:
            result = self.contains(elem)
            if result == True:
                setC.items.append(elem)
        return setC

    def __sub__(self,setB):
        setC = Set()
        for elem in self.items:
            result = setB.contains(elem)
            if result == False:
                setC.items.append(elem)
        return setC

    def isSubsetOf(self, setB):
        for elem in self.items:
            result = setB.contains(elem)
            if result == False:
                return print("setA는 setB의 부분 집합이 아닙니다.")
        return print("setA는 setB의 부분 집합입니다.")
                
    
setA = Set()
setA.insert("휴대폰")
setA.insert("지갑")
setA.insert("손수건")
setA.display("Set A: ")

setB = Set()
setB.insert("빗")
setB.insert("파이썬 자료구조")
setB.insert("야구공")
setB.insert("지갑")
setB.display("Set B: ")

setB.insert("빗")
setA.delete("손수건")
setA.delete("발수건")


setA.display("Set A: ")
setB.display("Set B: ")
setA.union(setB).display("A U B: ")
setA.intersect(setB).display("A ^ B: ")
(setA - setB).display("A - B: ")
setA.isSubsetOf(setB)