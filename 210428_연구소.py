from itertools import combinations
import copy
import sys
sys.stdin = open('input.txt','r')

# map 만들기
N, M = map(int,input().split())
G = []
zero_idx_list = []
for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)
    for idx, r in enumerate(row):
        if r == 0:
            zero_idx_list.append([i, idx])

# 안전영역 크기
def secure_area(graph):
    cnt = 0
    for row in graph:
        cnt += row.count(0)
    return cnt

# 바이러스 퍼진 후의 graph
def dfs(start_node, ):


def after_virus_graph(graph):

                    
                
    return graph

# combination
combi = combinations(zero_idx_list, 3)
answers = []
for zeros in combi:
    G_copy = copy.deepcopy(G)
    a, b, c = zeros[0], zeros[1], zeros[2]
    G_copy[a[0]][a[1]] = 1
    G_copy[b[0]][b[1]] = 1
    G_copy[c[0]][c[1]] = 1
    for row in G_copy:
        print(row)
    print()
    result = after_virus_graph(G_copy)
    for row in result:
        print(row)
    break
#     area = secure_area(result)
#     answers.append(area)
#     print(area)

# print('::::::::::::::')
# print(max(answers))