import random
array = []

for i in range(1000):
    a = random.randint(1,1000)
    
    if a in array:
        i -=1
    else:
        array.append(a)
print(array)    
print(len(array))
        