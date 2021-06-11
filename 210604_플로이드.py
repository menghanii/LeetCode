import sys
sys.stdin = open('input.txt','r')

n = int(input())
m = int(input())
g = [[1e+10]*(n+1) for _ in range(n+1)] # n개의 도시 -> n개의 list 반환.
for i in range(1, n+1):
    g[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if g[a][b] > c:
        g[a][b] = c

# print(g)
# Floyd
for i in range(1, n+1): # 거쳐갈 놈.
    for j in range(1, n+1): # 시작 노드
        for k in range(1, n+1): # 도착 노드
            # print(g[i][j])
            min_dist = min(g[j][k], g[j][i] + g[i][k])
            g[j][k] = min_dist

for i in g[1:]:
    print(' '.join(map(str, i[1:])))
    # print(i[1:])