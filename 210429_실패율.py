def solution(N, stages):
    result = dict()
    cnt = 0
    for i in range(1,N+1):
        num = stages.count(i)
        failure_rate = num/(len(stages) - cnt)
        result[i] = failure_rate
        cnt += num
    return [i[0] for i in sorted(result.items(), key=lambda x: (-x[1], x[0]))]
    

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))

