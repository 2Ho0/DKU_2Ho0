import decimal
n = int(input("피라미드의 높이를 입력하세요: "))
for i in range(n):
    num=1
    print(" "*(n-i)*2,end="")

    for j in range(i*2+1):
        if j>=round(decimal.Decimal((i*2+1)//2)):
            print(num, end=" ")
            num-=2
        elif j<=round(decimal.Decimal((i*2+1)//2)):
            print(num,end=" ")
            num+=2

    print()

        







    
        
        
        
    
        