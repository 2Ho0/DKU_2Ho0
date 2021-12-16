class read_poly:
    def __init__ (self):
        self.poly = []
        

    def degree(self):
        self.n = int(input("다항식의 최고 차수를 입력하시오: "))
        for i in range(self.n+1):
            self.poly.append(int(input("x^{}의 계수: ".format(i))))

    def eval(self,scalar):
        result = 0
        for i in range(len(self.poly)):
            if i==0:
                result+=self.poly[i]
            else:
                result += self.poly[i]*(scalar**i)
        return result

    def display(self,msg):
        print(msg,end="")
        for i in range(len(self.poly),0,-1):
            if i !=1:
                print("{0}x^{1} + ".format(self.poly[i-1],i-1),end="")
            else: 
                print("{0}".format(self.poly[i-1]))

    def add(self, b):
        c = read_poly()
        if len(self.poly)> len(b.poly):
            n = len(b.poly)
            c.poly = self.poly.copy()
            for i in range(n):
                c.poly[i]=c.poly[i]+b.poly[i]
            return c
        elif len(self.poly)< len(b.poly):
            n = len(self.poly)
            c.poly = b.poly.copy()
            for i in range(n):
                c.poly[i]=c.poly[i]+self.poly[i]
                print(c.poly)
            return c
        else:
            n = len(b.poly)
            c.poly = self.poly.copy()
            for i in range(n):
                c.poly[i]=c.poly[i]+b.poly[i]
            return c
    
    def sub(self, b):
        c = read_poly()
        if len(self.poly)> len(b.poly):
            n = len(b.poly)
            c.poly = self.poly.copy()
            for i in range(n):
                c.poly[i]=c.poly[i]-b.poly[i]
            return c
        elif len(self.poly)< len(b.poly):
            n = len(self.poly)
            c.poly = b.poly.copy()
            for i in range(n):
                c.poly[i]=self.poly[i]-c.poly[i]
            c.poly[-1] = -c.poly[-1]
            return c
        else:
            n = len(b.poly)
            c.poly = self.poly.copy()
            for i in range(n):
                c.poly[i]=c.poly[i]-b.poly[i]
            return c 

    def mul(self, b):
            c = read_poly()
            c.poly=[0]*(len(self.poly)+len(b.poly)-1)
            for i in range(len(self.poly)):
                for j in range(len(b.poly)):
                    c.poly[i+j]+=self.poly[i]*b.poly[j]
            return c



a = read_poly()
a.degree()
b = read_poly()
b.degree()
c = a.add(b)
d = a.sub(b)
e = a.mul(b)

a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")
d.display("D(x) = ")
e.display("E(x) = ")

print("C(2) = ", c.eval(2))
print("D(2) = ", d.eval(2))
print("E(2) = ", e.eval(2))
