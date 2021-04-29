num = int(input())
houses = list(map(int, input().split()))
print(sum(houses)//len(houses))