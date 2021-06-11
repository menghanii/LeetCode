def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [[], [2,5],[3,4],[],[],[]]
visited = [0] * 6
dfs(graph, v=1, visited=visited)