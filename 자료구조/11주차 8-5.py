from collections import deque
class TNode:
    def __init__ (self,data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left) + count_node(n.right)

def path_length(root,totalNodes):
    if (totalNodes == 1)or(totalNodes==0) :
        return 0;
    noOfNodes1 = count_node(root.left)
    noOfNodes2 = count_node(root.right)
    return ( path_length(root.left, noOfNodes1)
           + path_length(root.right, noOfNodes2) + totalNodes - 1)

def reverse(root):
    queue = deque([root])
    while queue:
        node = queue.popleft() # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

c = TNode('C', None, None)
d = TNode('D', None, None)
b = TNode('B', c, d)
f = TNode('F', None, None)
e = TNode('E', f, None)
root = TNode('A', b, e)

print("path length: ", path_length(root,count_node(root))) # should be 8


reversed_tree = reverse(root)
inorder(reversed_tree) # E-F-A-D-B-C 