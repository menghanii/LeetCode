from collections import deque

graph = [[], [2, 5], [3, 4], [], [], []]
# BFS
def bfs(graph, start, visited):
    # queue 만들고 start 삽입
    q = deque([start])
    # visited 방문처리
    visited[start] = True
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

bfs(graph, 1, [False]*6)