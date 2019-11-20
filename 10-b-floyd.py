import sys
maxint = sys.maxsize
a = maxint
def floyd(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                graph[j][k] = min(graph[j][k],graph[j][i]+graph[i][k])

    return graph


graph = [[0,2,a,1,8],
         [6,0,3,2,a],
         [a,a,0,4,a],
         [a,a,2,0,3],
         [3,a,a,a,0]]


print(floyd(graph))
