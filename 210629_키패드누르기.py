def solution(numbers, hand):
    answer = ''
    pad = {1: (0, 0), 2: (0, 1),3: (0, 2),
           4: (1, 0), 5: (1, 1),6: (1, 2),
           7: (2, 0), 8: (2, 1),9: (2, 2),
           '*': (3, 0),0: (3, 1),'#': (3, 2)}
    l_loc = (3, 0)
    r_loc = (3, 2)
    for num in numbers:
        # [1,4,7], [3,6,9] -> LR 및 현재 위치
        if num in [1,4,7]:
            answer += 'L'
            l_loc = pad[num]
        elif num in [3,6,9]:
            answer += 'R'
            r_loc = pad[num]
        else: # [2,5,8,0] -> 거리 구하기
            l_dist = abs((l_loc[0] - pad[num][0])) + abs((l_loc[1] - pad[num][1]))
            r_dist = abs((r_loc[0] - pad[num][0])) + abs((r_loc[1] - pad[num][1]))
            if l_dist < r_dist:
                answer += 'L'
                l_loc = pad[num]
            elif l_dist > r_dist:
                answer += 'R'
                r_loc = pad[num]
            else:
                if hand == 'right':
                    answer += 'R'
                    r_loc = pad[num]
                else:
                    answer += 'L'
                    l_loc = pad[num]

    return answer