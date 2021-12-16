class BSTNode:				            
    def __init__ (self, key, value):	
        self.key = key		        	
        self.value = value	          	
        self.left = None		    	
        self.right = None
        
class PQueueWithBST :
    def __init__( self ):					
        self.items = []
        self.root = None					

    def isEmpty (self): return self.root == None
    def size(self): return count_node(self.root)
    def clear(self): self.root = None
    
    def enqueue(self, key, value=None):	
        n = BSTNode(key, value)		    
        if self.isEmpty() :		        
           self.root = n
           self.items.append(n.key)			    
        else :				            
           self.iterative_insert_bst(self.root, n)
           	       			       	
    def dequeue( self ):		
        highest = search_max_bst(self.root)
        self.root = delete_bst (self.root, highest.key)		
        if highest is not None :
            return self.items.pop(self.items.index(highest.key))	

    def peek( self ):				
        highest = search_max_bst()	
        if highest is not None :
            return self.items[highest]
        
    def iterative_insert_bst(self,r,n):
        while n != None:
            if n.key < r.key:
                if r.left is None:
                    r.left = n
                else:
                    r = r.left
            elif n.key> r.key:
                if r.right is None:
                    r.right = n
                else:
                    r = r.right  
            else:
                break
        self.items.append(n.key)
    
def search_max_bst(n) :	
    while n != None and n.right != None:
        n = n.right
    return n

def delete_bst_case1 (parent, node, root) :
    if parent is None: 			    
        root = None			        
    else :
        if parent.left == node : 	
            parent.left = None		
        else :				        
            parent.right = None		

    return root			            

def delete_bst_case2 (parent, node, root) :
    if node.left is not None :	
        child = node.left		
    else :						
        child = node.right		

    if node == root :			
        root = child			
    else :
        if node is parent.left : 	
            parent.left = child		
        else :			        	
            parent.right = child	

    return root	

def delete_bst_case3 (parent, node, root) :
    succp = node		        	
    succ = node.right		    	
    while (succ.left != None) :		
        succp = succ			
        succ = succ.left

    if (succp.left == succ) :		
        succp.left = succ.right		
    else :			            	
        succp.right = succ.right	

    node.key = succ.key	    		
    node.value= succ.value	    	
    node = succ;			        

    return root

def delete_bst (root, key) :
    if root == None : return None       		

    parent = None                       		
    node = root                         	    
    while node != None and node.key != key :	
        parent = node
        if key < node.key : node = node.left
        else : node = node.right;

    if node == None : return None       		
    if node.left == None and node.right == None:
        root = delete_bst_case1 (parent, node, root)
        return root
    elif node.left==None or node.right==None :	
        root = delete_bst_case2 (parent, node, root)
        return root
    else :
        root = delete_bst_case3 (parent, node, root)
        return root
        
def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left) + count_node(n.right)
        
q = PQueueWithBST()
q.enqueue( 34 )
q.enqueue( 18 )
q.enqueue( 27 )
q.enqueue( 45 )
q.enqueue( 15 )
q.enqueue( 50 )
q.enqueue( 60 )

print("PQueueWithBST:", q.items)
while not q.isEmpty() :
    print("Max Priority = ", q.dequeue())