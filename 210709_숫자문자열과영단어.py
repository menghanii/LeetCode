def solution(s):
    answer = ''
    num_dict = {'zero':0, 'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
                'seven': 7, 'eight':8, 'nine': 9}
    num = ''
    for letter in s:
        if letter.isdigit():
            answer += letter
        else:
            num += letter
            if num in num_dict.keys():
                answer += str(num_dict[num])
                num = ''
    return int(answer)