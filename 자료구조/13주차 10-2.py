from collections import deque

def matGraphBFS(ver,graph,start,visited=[]):
  visited.append(start)
  queue=deque()
  queue.append(start)
  i=0
  j=0
  while queue:
    while(ver[i]!=queue[0]):
        i=i+1
    a=queue.popleft()
    print(a,end=' ')
    for j in range(len(ver)):
      if((graph[i][j]==1) and (ver[j] not in visited)):
        queue.append(ver[j])
        visited.append(ver[j])
        j=j+1
      else:
        j=j+1
    i=0
  
vertex = ['0', '1', '2', '3', '4', '5', '6', '7','8','9']
graphAM = [ [ 0,   1,   0,   0,   0,   0,   0,   0,  0,  0],
            [ 1,   0,   1,   1,   0,   0,   0,   0,  0,  0 ],
            [ 0,   1,   0,   0,   1,   0,   0,   0,  0,  0 ],
            [ 0,   1,   0,   0,   1,   1,   0,   0,  0,  0 ],
            [ 0,   0,   1,   1,   0,   0,   0,   0,  0,  0 ],
            [ 0,   0,   0,   1,   0,   0,   1,   1,  0,  0 ],
            [ 0,   0,   0,   0,   0,   1,   0,   1,  0,  0 ], 
            [ 0,   0,   0,   0,   0,   1,   1,   0,  1,  1 ],
            [ 0,   0,   0,   0,   0,   0,   0,   1,  0,  0 ],
            [ 0,   0,   0,   0,   0,   0,   0,   1,  0,  0 ]]
            
# vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]
# graphAM = [ [ 0,   1,   1,   0,   0,   0,   0,   0 ],
#             [ 1,   0,   0,   1,   0,   0,   0,   0 ],
#             [ 1,   0,   0,   1,   1,   0,   0,   0 ],
#             [ 0,   1,   1,   0,   0,   1,   0,   0 ],
#             [ 0,   0,   1,   0,   0,   0,   1,   1 ],
#             [ 0,   0,   0,   1,   0,   0,   0,   0 ],
#             [ 0,   0,   0,   0,   1,   0,   0,   1 ], 
#             [ 0,   0,   0,   0,   1,   0,   1,   0 ] ]

matGraphBFS(vertex, graphAM, '3')