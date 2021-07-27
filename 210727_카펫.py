def find_possible_numbers(number):
    result = []
    for i in range(1, int(number ** 0.5)+1):
        div_mod = divmod(number, i)
        if div_mod[1] == 0:
            result.append([i, div_mod[0]])
    return result

def solution(brown, yellow):
    answer = []
    area = brown + yellow
    nums = find_possible_numbers(area)
    for n in nums:
        if brown == (n[1] * 2) + ((n[0]-2) * 2):  # brown
            answer = n
            break
    return answer[::-1]