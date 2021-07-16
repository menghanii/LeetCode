#210716 still not resolved
def solution(numbers, target):
    size = len(numbers)
    answer = 0
    
    cnt = 0
    arr = []
    for n in range(len(numbers)):
        for i in [1, -1]:
            arr.append(n * i)
    return answer

solution([1,1,1,1,1], 5)
