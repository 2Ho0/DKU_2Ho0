def draw_tree(row,left,right):
    print("-"*left,end="")
    print("X",end="")
    print("-"*right,end="")

    
for i in range(6):
    for j in range((2**i)):
        draw_tree(i,2**(5-i)-1, 2**(5-i))
    print()