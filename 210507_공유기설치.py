num_home, num_iptime = map(int, input().split())
lst = []
for i in range(num_home):
    lst.append(int(input()))
lst.sort()

def install_iptime(start, end, cnt=num_iptime-2):
    mid = (start+end) // 2
    if lst[end] - lst[mid] >
    distance = min(lst[end]-lst[mid], lst[mid]-lst[start])
    cnt -= 2
    if cnt <= 0:
        return distance
    