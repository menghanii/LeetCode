t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = [arr[m*i:m*(i+1)] for i in range(n)]
    
    for i in range(1, m): # column
        for j in range(n): # row
            if j == 0:
                arr[j][i] += max(arr[j][i-1], arr[j+1][i-1])
            elif j == n-1:
                arr[j][i] += max(arr[j-1][i-1], arr[j][i-1])
            else:
                arr[j][i] += max(arr[j-1][i-1], arr[j][i-1], arr[j+1][i-1])

    print(max([a[-1] for a in arr]))