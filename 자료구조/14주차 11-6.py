INF = 9999
def choose_vertex(dist, found) :			
    min = INF
    minpos = -1
    for i in range(len(dist)) :				
        if dist[i]<min and found[i]==False:	
            min = dist[i]
            minpos = i
    return minpos;							

def dijkstra_SP_with_path_print(graph,start=0) :
    vtx = graph[0]
    adj = graph[1]
    vsize = len(vtx)						
    dist = list(adj[start])					
    path = [start] * vsize					
    found= [False] * vsize					
    found[start] = True						
    dist[start] = 0							

    for i in range(vsize) : 	
        u = choose_vertex(dist, found)		
        found[u] = True						

        for w in range(vsize) :				
            if not found[w] :				
                if dist[u] + adj[u][w] < dist[w] :	
                    dist[w] = dist[u] + adj[u][w]	
                    path[w] = u						

    print("Src->Dst \t Dist\t Path")
    end = 0
    count = 1
    next = []
    for start in range(len(vertex)):
        
        if start != end:
            print("A -> %s\t\t" %vertex[count], end=' ')
            print(dist[count],"\t", end=" ")
            print(vertex[0], end=' ')
            while(path[start]!=end):
                next.append(vertex[path[start]])
                start = path[start]
            for _ in range(len(next)):
                a = next.pop()
                print(a, end =' ')
            print(vertex[count])
            count+=1						            

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' 	]
weight = [ [0,	    7,		INF,		INF,		3,      10,		INF	],
           [7,		0,	    4,		10,	    2,	    6,	    INF	],
           [INF,	4,		0,		2,		INF,		INF,		INF	],
           [INF,	10,		2,		0,      11,		9,		4   ],
           [3,	    2,	    INF,   	11,		0,      13,		5   ],
           [10,	6,	    INF,		9,      13,		0,		INF	],
           [INF,   INF,		INF,   	4,		5,		INF,		0   ] ]    
graph = (vertex, weight)
dijkstra_SP_with_path_print(graph)