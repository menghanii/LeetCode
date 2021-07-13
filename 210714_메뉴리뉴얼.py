from itertools import combinations
from collections import defaultdict

# 3중 for문 말고 다른 방법으로 풀 수는 없을까..
def solution(orders, course):
    answer = []
    for c in course:
        menu = defaultdict(int)
        for o in orders:
            for combi in combinations(sorted(list(o)),c): # combination할 때 알파벳 순서 맞춰줘야함.
                combi_str = ''.join(list(combi))
                menu[combi_str] += 1
        if len(menu) == 0: # ex) course에 4가 있는데 모든 사람이 메뉴 3개만 먹은 경우
            max_vote = 0
        else:
            max_vote = max(menu.values())
        if max_vote >= 2: # 2명 이상이 먹은 경우에 한함.
            for k, v in menu.items():
                if v == max_vote:
                    answer.append(k)
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))