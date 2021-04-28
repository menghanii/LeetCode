from collections import defaultdict, deque
N, M, K, X = tuple(map(int, input().split()))
G = defaultdict(list)
for _ in range(M):
    start, end = tuple(map(int, input().split()))
    G[start].append(end)

visited = [False] * (N+1)
def bfs(q = deque([X]), target=K, cnt=1):
    temp = []
    for node in q:
        visited[node] = True
    while q:
        a = q.popleft()
        for i in G[a]:
            if not visited[i]:
                temp.append(i)
    if cnt == K:
        if len(temp) == 0:
            print(-1)
        else:
            temp.sort()
            for t in temp:
                print(t)
    else:
        cnt += 1
        bfs(temp, target, cnt)

bfs()