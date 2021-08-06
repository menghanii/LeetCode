# 먼저 최대한 2명을 태우는 방법을 고민해야함.
# limit / 2를 기준으로 left와 right로 나눈 다음에 계산.
def solution(people, limit):
    answer = 0
    st = limit / 2
    left = []
    right = []
    for p in people:
        if p <= st:
            left.append(p)
        else:
            right.append(p)
    left.sort()
    right.sort()
    while left and right:
        l = left[0]
        r = right.pop()
        if l + r <= limit:
            left.pop(0)
            answer += 1
        else:
            answer += 1
    answer += len(right)
    div, mod = divmod(len(left), 2)
    answer += div + mod
    return answer

print(solution([40, 40, 50, 60], 100))