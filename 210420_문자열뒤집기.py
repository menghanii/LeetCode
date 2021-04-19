# 111001100111인 경우, 4~5번째, 8~9번째에 있는 00을 뒤집으면 2번만에 같은 숫자로 만들 수 있음.
# [111, 00, 11, 00, 111] 으로 만들어주는 방법?
string = input()
cnt = 0
prev = string[0] # 비교할 바로 앞 number
for st in string[1:]:
    if st == prev: # 같으면 넘어가고
        continue
    else: # 다르면 cnt += 1
        cnt += 1
        prev = st

print(cnt//2) # 2로 나눈 몫이 최소값
        