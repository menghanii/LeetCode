num = int(input('모험가는 몇 명?'))
horror_list = sorted(list(map(int, input('공포도를 나열하세용.').split())))
cnt = 0
group = []
for _ in range(len(horror_list)):
    horror = horror_list.pop(0)
    group.append(horror)
    if len(group) < max(group): # 그룹의 인원수와 그룹 내 max 공포도를 비교
        continue
    else:
        cnt += 1
        group = []
print(cnt)