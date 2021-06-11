# list[mid] == mid 인지 확인
# list[mid] < mid 인 경우 오른쪽 확인
# list[mid] > mid 인 경우 왼쪽 확인
num = input()
lst = list(map(int, input().split()))
def find_fix_point(start, end):
    if start > end: # mid+-1 로 start index가 end index를 넘어가는 경우 : 종료조건
        return -1
    mid = (start+end) // 2
    if lst[mid] == mid:
        return mid
    elif lst[mid] < mid:
        return find_fix_point(mid+1, end)
    else:
        return find_fix_point(start, mid-1)

print(find_fix_point(0, len(lst)-1))