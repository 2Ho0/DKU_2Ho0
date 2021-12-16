def bubble_sort(A) :					
    n = len(A)
    for i in range(n-1, 0, -1) :		
        bChanged = False
        for j in range (i) :			
            if (A[j]>A[j+1]) :			
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True		

        if not bChanged: break;		
        printStep(A, n - i);

def printStep(arr, val) :					
    print("  Step %2d = " % val, end='')
    print(arr)

data = [9,6,7,3,5]
print("Original  :", data)
bubble_sort(data)
print("Selection :", data)