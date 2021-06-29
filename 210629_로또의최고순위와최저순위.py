def solution(lottos, win_nums):
    correct = 0
    unknown = 0
    for l in lottos:
        if l == 0:
            unknown += 1
        elif l in win_nums:
            correct += 1
        else:
            continue
    best = correct + unknown
    worst = correct
    answer_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer = [answer_dict[best], answer_dict[worst]]
    return answer