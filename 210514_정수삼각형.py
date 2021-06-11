n = int(input())
arr = []
for i in range(n):
    arr.append(list((map(int, input().split()))))

for row in range(1, n):
    for idx in range(len(arr[row])):
        if idx == 0:
            arr[row][idx] += arr[row-1][0]
        elif idx == len(arr[row])-1:
            arr[row][idx] += arr[row-1][len(arr[row])-2] # 이전 row는 이번 row보다 원소가 1개 적으므로, 마지막 인덱스가 len(arr[row]) - 2
        else:
            arr[row][idx] += max(arr[row-1][idx-1], arr[row-1][idx])

print(max(arr[-1]))

