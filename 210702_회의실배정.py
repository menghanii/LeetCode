import sys
sys.stdin = open('./input.txt', 'r')

conferences = []
N = int(input())
for _ in range(N):
    time = list(map(int, input().split()))
    conferences.append(time)
conferences.sort(key=lambda x : (x[1], x[1]-x[0])) # 끝나는 시간이 짧은 순서대로 -> 회의 시간이 짧은 순서대로.
reserved = [conferences[0]]
for conference in conferences[1:]:
    start = conference[0]
    if reserved[-1][1] <= start:
        reserved.append(conference)
print(len(reserved))

