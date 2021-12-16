from collections import deque

def matGraphSpanningTreeDFS(ver,graph,start,visited=[]):
    if start not in visited:
        visited.append(start)
        near=[]
        i=ver.index(start)
        j=0
        while(j<len(ver)):
            if((graph[i][j]==1) and (ver[j] not in visited)):
                near.append(ver[j])
                j=j+1
            else:
                j=j+1
                
        for u in near:
            if u not in visited:
                print("(",start,",",u,")", end="")
                matGraphSpanningTreeDFS(ver,graph,u,visited)
            



vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]
graphAM = [ [ 0,   1,   1,   0,   0,   0,   0,   0 ],
            [ 1,   0,   0,   1,   0,   0,   0,   0 ],
            [ 1,   0,   0,   1,   1,   0,   0,   0 ],
            [ 0,   1,   1,   0,   0,   1,   0,   0 ],
            [ 0,   0,   1,   0,   0,   0,   1,   1 ],
            [ 0,   0,   0,   1,   0,   0,   0,   0 ],
            [ 0,   0,   0,   0,   1,   0,   0,   1 ], 
            [ 0,   0,   0,   0,   1,   0,   1,   0 ] ]

matGraphSpanningTreeDFS(vertex, graphAM, 'A')