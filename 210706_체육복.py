def solution(n, lost, reserve):
    answer = n - len(lost)
    residual = []
    while len(reserve):
        r = reserve.pop()
        if r in lost:
            answer += 1
            lost.remove(r)
        else:
            residual.append(r)
    for r in residual:
        if (r-1) in lost:
            answer += 1
            lost.remove(r-1)
        elif (r+1) in lost:
            answer += 1
            lost.remove(r+1)
    return answer