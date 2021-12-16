# from collections import deque

# def matGraphFindBridge(ver,graph,start,visited=[]):
#     # if start not in visited:
#         visited.append(start)
#         near=[]
#         i=ver.index(start)
#         j=0
#         while(j<len(ver)):
#             if((graph[i][j]==1) and (ver[j] not in visited)):
#                 near.append(ver[j])
#                 j=j+1
#             else:
#                 j=j+1
                
#         for u in near:
#             # if u not in visited:
#                 print("(",start,",",u,")", end="")
#                 matGraphFindBridge(ver,graph,u,visited)

# from collections import deque

# def matGraphFindBridge(ver,graph,start,visited=[]):
#   visited.append(start)
#   queue=deque()
#   queue.append(start)
#   i=0
#   j=0
#   bridge = []
#   while queue:
#     near=[]
#     while(ver[i]!=queue[0]):
#         i=i+1
#     a=queue.popleft()
#     print(a,end=' ')
#     for j in range(len(ver)):
#       if((graph[i][j]==1) and (ver[j] not in visited)):
#         queue.append(ver[j])
#         visited.append(ver[j])
#         near.append(ver[j])
#         j=j+1
#       elif (graph[i][j]==1) and (ver[j] in visited) :
#           near.append(ver[j])
#           j=j+1
#       else:
#         j=j+1

#     i=0
    
#     for u in near:
#             bridge.append([a,u])
#   print(bridge)
# from collections import deque

# def matGraphFindBridge(ver,graph,start,visited=[],):
#     visited.append(start)
#     near=[]
#     i=ver.index(start)
#     j=0
#     while(j<len(ver)):
#         if((graph[i][j]==1) and (ver[j] not in visited)):
#             near.append(ver[j])
#             j=j+1
#         else:
#             j=j+1
            
#     for u in near:
#             matGraphFindBridge(ver,graph,u,visited)
#             print("(",start,",",u,")", end="")

def labelDFS(g, v, color, vis):
    vis[v] = True
    
    for j in range(0, len(vis)):
        if (g[v][j] == 1) and (vis[j] == False):
            labelDFS(g, j, color, vis)

def findConnectedComponent(ver, g, vis):
    count = 0
    for i in range(len(ver)):
      if vis[i] == False:
        count += 1
        labelDFS(g, i, count, vis)
        
    return count

def matGraphFindBridge(ver, g):
    visited = [False] * len(ver)
    
    for i in range(0, len(ver)):
        for j in range(0, i):
            if g[i][j] != 0:
                g[i][j] = 0
                g[j][i] = 0
    
                visited = [False] * len(ver)
                if findConnectedComponent(ver, g, visited) > 1:
                    print("(",ver[j],",",ver[i],")", end=' ')
                g[i][j] = 1
                g[j][i] = 1     

vertex = ['A', 'B', 'C', 'D', 'E', 'F' ]
graphAM = [ [ 0,   1,   0,   1,   0,   0],
            [ 1,   0,   1,   1,   1,   0],
            [ 0,   1,   0,   0,   0,   1],
            [ 1,   1,   0,   0,   1,   0],
            [ 0,   1,   0,   1,   0,   0],
            [ 0,   0,   1,   0,   0,   0]]

matGraphFindBridge(vertex, graphAM)