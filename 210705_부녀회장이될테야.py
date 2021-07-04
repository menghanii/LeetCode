def calculate_ppl(k, n):
    floor = 1
    status = list(range(1, n+1)) # 0층 n호까지 사람의 수
    while floor != k:
        answer = []
        men = 0
        for s in status:
            men += s
            answer.append(men)
        status = answer
        floor += 1
    return sum(status)

T = int(input())
for _ in range(T):
    lst = []
    for _ in range(2):
        lst.append(int(input()))
    k = lst[0]
    n = lst[1]
    print(calculate_ppl(k, n))