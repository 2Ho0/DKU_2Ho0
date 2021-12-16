class TNode:								
    def __init__ (self, data, left, right):	
        self.data = data 					
        self.left = left					
        self.right = right
MAX_QSIZE = 20			    
class CircularQueue :
    def __init__( self ) :		
        self.front = 0			
        self.rear = 0			
        self.items = [None] * MAX_QSIZE	

    def isEmpty( self ) : return self.front == self.rear
    def isFull( self ) : return self.front == (self.rear+1)%MAX_QSIZE
    def clear( self ) : self.front = self.rear

    def enqueue( self, item ):
        if not self.isFull():			            
            self.rear = (self.rear+1)% MAX_QSIZE	
            self.items[self.rear] = item		    

    def dequeue( self ):
        if not self.isEmpty():			            
            self.front = (self.front+1)% MAX_QSIZE	
            return self.items[self.front]	        

    def peek( self ):
        if not self.isEmpty():
            return self.items[(self.front + 1) % MAX_QSIZE]

    def size( self ) :
       return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE

    def display( self ):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] \
                + self.items[0:self.rear+1]		
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)
        
def preorder(n) :				
    if n is not None :
        print(n.data, end=' ')	
        preorder(n.left)		
        preorder(n.right)		

def inorder(n) :				
    if n is not None :
        inorder(n.left)			
        print(n.data, end=' ')	
        inorder(n.right)		

def postorder(n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')


def levelorder(root) :
    queue = CircularQueue()			
    queue.enqueue(root)				
    while not queue.isEmpty() :		
        n = queue.dequeue()			
        if n is not None :
            print(n.data, end=' ')	
            queue.enqueue(n.left)	
            queue.enqueue(n.right)	

def count_node(n) :
    if n is None : 
        return 0
    else : 			
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n) :
    if n is None :	
        return 0
    elif n.left is None and n.right is None :
        return 1
    else : 		
        return count_leaf(n.left) + count_leaf(n.right)


def calc_height(n) :
    if n is None : 					
        return 0
    hLeft = calc_height(n.left)		
    hRight = calc_height(n.right)	
    if (hLeft > hRight) : 			
        return hLeft + 1
    else: 
        return hRight + 1


a = TNode('1', None, None)
c = TNode('3', None, None)
b = TNode('2', a, c)
e = TNode('5', None, None)
d = TNode('4', b, e)
h = TNode('8', None, None)
k = TNode('11', None, None)
j = TNode('10', h, k)
g = TNode('7', None, None)
i = TNode('9', g, j)
root = TNode('6', d, i)

print('\n   In-Order : ', end='')
inorder(root)
print('\n  Pre-Order : ', end='')
preorder(root)
print('\n Post-Order : ', end='')
postorder(root)
print('\nLevel-Order : ', end='')
levelorder(root)
print()

print(" 노드의 개수 = %d개" % count_node(root))
print(" 단말의 개수 = %d개" % count_leaf(root))
print(" 트리의 높이 = %d" % calc_height(root))