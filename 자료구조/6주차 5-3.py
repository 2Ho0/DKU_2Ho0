from queue import Queue
def myFibonacci(n):
    que = Queue()
    que.put(1)
    que.put(1)

    sum=0

    for i in range(2,n):
        a=que.get()
        b=que.get()
        sum = a+b
        que.put(b)
        que.put(sum)
    print(sum)

myFibonacci(10)

