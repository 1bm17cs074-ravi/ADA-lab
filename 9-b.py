def prims(graph):
    sum = 0
    ans = [[0 for i in range(len(graph))] for j in range(len(graph))]
    visited = [False]*len(graph)
    for i in range(len(graph)):
        visited[i] = True
        for j in range(len(graph)):
            if not visited[j] and graph[i][j] != 999:
                sum+=graph[i][j]
                ans[i][j] = 1
                visited[j] = True
    return (ans,sum)

graph = [
    [999,4,2,999,999,999],
    [4,999,4,999,999,999],
    [2,4,999,3,4,2],
    [999,999,4,3,999,3],
    [999,999,2,999,3,999],
    

    ]

a,s = prims(graph)

print(a)
print(s)
                
                
