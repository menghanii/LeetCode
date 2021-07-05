def solution(absolutes, signs):
    sum = 0
    for i, j in zip(absolutes, signs):
        if j == False:
            sum -= i
        else:
            sum += i
    return sum