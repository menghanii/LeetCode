def solution(s):
    a = list(map(int, s.split()))
    return f'{min(a)} {max(a)}'

print(solution("1 2 3 4"))