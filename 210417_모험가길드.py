# 가장 높은 공포도 = n -> 내림차순으로 n명

num = int(input('모험가는 몇 명?'))
horror_list = sorted(list(map(int, input('공포도를 나열하세용.').split())), reverse=True)
guild_sum = 0 # (앞으로 더해질) 모험가의 수
cnt = 0
while guild_sum < len(horror_list): # 모험가 수 더한 값 < 전체 모험가 수
    cnt += 1
    guild_sum += horror_list[guild_sum]

print(cnt)