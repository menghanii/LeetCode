# 2진법을 활용한 풀이
def solution(numbers, target):
    n = len(numbers)
    binary2plusminus = {'0': 1, '1': -1}
    binaries = []
    result = []
    for i in range(2**n):
        binary = bin(i)[2:]
        binary = '0' * (n - len(binary)) + binary
        binaries.append([binary2plusminus[b] for b in binary])
    for b_list in binaries:
        res = 0
        for i, j in zip(numbers, b_list):
            res += (i * j)
        result.append(res)
    return result.count(target)


## 프로그래머스 dfs 풀이
def solution(numbers, target):
    result = 0
    def dfs(num, level):
        nonlocal result

        if level == len(numbers):
            if num == target:
                result += 1
            return

        signs = [-num, num]
        if level == 1:
            for i in range(2):
                dfs(signs[i] + numbers[level], level + 1)
                dfs(signs[i] - numbers[level], level + 1)
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0], 1)
    return result