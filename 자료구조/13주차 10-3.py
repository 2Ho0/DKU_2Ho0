from collections import deque
def matGraphFindConnectedGrapth(graph, vertex) :
    visited = []					
    colorList = []					
    for vtx in vertex :				
        if vtx not in visited :		
            color = bfs_cc(graph, [],vtx, visited)	
            colorList.append( color )	

    print("그래프 연결성분 개수 = %d " % len(colorList))
    print(colorList)				        

def bfs_cc(graph, color, vtx,visited):
    ver = ['A', 'B', 'C', 'D', 'E']
    visited.append(vtx)
    queue=deque()
    queue.append(vtx)
    
    i=0
    j=0
    while queue:
        while(ver[i]!=queue[0]):
            i=i+1
        a=queue.popleft()
        color.append(a)
        for j in range(len(ver)):
            if((graph[i][j]==1) and (ver[j] not in visited)):
                queue.append(ver[j])
                visited.append(ver[j])
                j=j+1
            else:
                j=j+1
        i=0
    return color
    		    

vertex = ['A', 'B', 'C', 'D', 'E' ]
graphAM = [ [ 0,   1,   1,   0,   0],
            [ 1,   0,   0,   0,   0],
            [ 1,   0,   0,   0,   0],
            [ 0,   0,   0,   0,   1],
            [ 0,   0,   0,   1,   0]]

matGraphFindConnectedGrapth(graphAM, vertex)
