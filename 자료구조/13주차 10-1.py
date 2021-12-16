def matGraphDFS(ver,graph,start,visited=[]):
      if start not in visited:
        visited.append(start)
        print(start,end=' ')
        near=[]
        i=ver.index(start)
        j=0
        while(j<len(ver)):
            if((graph[i][j]==1) and (ver[j] not in visited)):
                near.append(ver[j])
                j=j+1
            else:
                j=j+1
        
        for v in near:
            matGraphDFS(ver,graph,v,visited)

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

matGraphDFS(vertex, graphAM, '3')