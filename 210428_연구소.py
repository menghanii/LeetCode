from itertools import combinations
import copy
import sys
import time

sys.stdin = open('input.txt','r')

start = time.time()
# map 만들기
N, M = map(int,input().split())
G = []
zero_idx_list = []
two_idx_list = []
for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)
    for idx, r in enumerate(row):
        if r == 0:
            zero_idx_list.append([i, idx])
        elif r == 2:
            two_idx_list.append([i, idx])

# print(f'zero_list:{zero_idx_list}')
# print(f'two_list:{two_idx_list}')

# 안전영역 크기
def secure_area(graph):
    cnt = 0
    for row in graph:
        cnt += row.count(0)
    return cnt

# 바이러스 퍼진 후의 graph

def dfs(graph, row, col, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    # 만약 start = 2라면 의 왼/오/위/아래 순으로 1만날때까지 dfs.
    visited[row][col] = 1
    graph[row][col] = 2
    # print(graph)
    for x, y in zip(dx, dy):
        # print(row+x,col+y)
        if row+x < 0 or row+x > N-1 or col+y < 0 or col+y > M-1:
            # print('continue!')
            continue
        else:
            if graph[row+x][col+y] == 1: # 벽이면
                continue
            else:
                if not visited[row+x][col+y]:
                    dfs(graph, row+x, col+y, visited)

# dfs([[0,0,0,0,0] for _ in range(5)], 0, 0, [[0,0,0,0,0] for _ in range(5)])
    
# combination
combi = combinations(zero_idx_list, 3)
answers = []
for zeros in combi:
    G_copy = copy.deepcopy(G)
    a, b, c = zeros[0], zeros[1], zeros[2]
    G_copy[a[0]][a[1]] = 1
    G_copy[b[0]][b[1]] = 1
    G_copy[c[0]][c[1]] = 1
    visited = [[0]*M for _ in range(N)]
    for two in two_idx_list:
        dfs(G_copy, two[0], two[1], visited)
    area = secure_area(G_copy)
    answers.append(area)

print(max(answers))

duration = time.time() - start 
print(duration)