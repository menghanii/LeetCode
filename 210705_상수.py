# 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
A, B = input().split()
print(max(int(A[::-1]), int(B[::-1])))