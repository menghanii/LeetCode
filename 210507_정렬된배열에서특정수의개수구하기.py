import sys
sys.stdin = open('input.txt','r')

cnt, target = map(int, input().split())
numbers = list(map(int, input().split()))

# [1, 1, 2, 2, 2, 2, 3] -> 7
def find_start_idx(start, end):
    mid = (start+end) // 2
    if (mid == 0 or numbers[mid-1] != target) and numbers[mid] == target:
        return mid
    elif numbers[mid] >= target: # 찾고자 하는 값이 같거나 더 작은 경우 -> 왼쪽 살펴봐야 함.
        return find_start_idx(start, mid-1)
    elif numbers[mid] < target:
        return find_start_idx(mid+1, end)
        
print(find_start_idx(0, cnt))


