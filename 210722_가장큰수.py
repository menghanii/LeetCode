def solution(numbers):
    answer = ''
    numbers = [str(n) for n in numbers]
    new = []
    original_lengths = []
    for i in range(len(numbers)):
        temp = ''
        origin_len = len(numbers[i])
        while len(temp) < 4:
           temp += numbers[i]
        new.append([temp[:4], origin_len])
    new.sort(key=lambda x : x[0], reverse=True)
    for n in new:
        answer += n[0][:n[1]]
    return str(int(answer))

print(solution([0, 0]))

# edge case 1 : [12, 121, 12]
# edge case 2 : [21, 212, 21]
# edge case 3 : [0, 0, 0]


# 기존풀이
'''
def solution(numbers):
    answer = ''
    numbers = sorted([str(n) for n in numbers], reverse=True)
    num_dict = dict()
    for n in numbers:
        if n[0] not in num_dict.keys():
            num_dict[n[0]] = [(n,len(n))]
        else:
            num_dict[n[0]].append((n,len(n)))
    for k, v in num_dict.items():
        answer += new_sort(k, v)
    return answer

# 길이 되는대로 비교 후, 더 긴 수의 남는 부분은 짧은 수의 제일 앞부분과 비교
def new_sort(key, num_list):
    result = ''
    max_len = max([i[1] for i in num_list])
    new_list = []
    for n in num_list:
        new_num = ''
        while len(new_num) < max_len:
            new_num += n[0]
        new_list.append([new_num[:max_len], n[1]])
    new_list.sort(key=lambda x: x[0], reverse=True)
    idxs = []
    lens = []
    for i in range(1, len(new_list)):
        if new_list[i][0] == new_list[i-1][0] and new_list[i][1] != 1 and new_list[i-1][1] != 1:
            if new_list[i][0][-1] < new_list[i][0][-2] :
                if len(idxs) == 0:
                    idxs.append(i-1)
                    idxs.append(i)
                    lens.append(new_list[i-1][1])
                    lens.append(new_list[i][1])
                else:
                    idxs.append(i)
                    lens.append(new_list[i][1])
        else:
            lens.sort()
            for i,j in zip(idxs, lens):
                new_list[i][1] = j
            idxs = []
            lens = []
    if len(idxs):
        lens.sort()
        for i,j in zip(idxs, lens):
            new_list[i][1] = j 
    for n in new_list:
        result += n[0][:n[1]]

    return result
'''
    



