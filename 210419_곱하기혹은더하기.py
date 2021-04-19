# 0과 1은 더하기, 나머지 숫자는 곱하기
# max_value가 0이면 다음 숫자는 무조건 더해야함.
value_list = list(map(int, list(input())))
max_value = 0
for v in value_list:
    if max_value == 0:
        max_value += v
    else:
        if v == 0 or v == 1:
            max_value += v
        else:
            max_value *= v
print(max_value)