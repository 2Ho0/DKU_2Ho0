class Bag:
    def __init__(self):
        self.itemlist = []
    def insert(self, item):
        self.itemlist.append(item)
    def bag(self):
        return self.itemlist
    def remove(self,item):
        self.itemlist.remove(item)


myBag = Bag()
myBag.insert("휴대폰")
myBag.insert("지갑")
myBag.insert("손수건")
myBag.insert("빗")
myBag.insert("자료구조")
myBag.insert("야구공")
print("내 가방속의 물건: ", myBag.bag())

myBag.insert("빗")
myBag.remove("손수건")
print("내 가방속의 물건: ", myBag.bag())
