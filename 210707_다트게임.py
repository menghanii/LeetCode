import re
def solution(dartResult):
    splitted = re.compile('[0-9]+[A-Z][*#]?').findall(dartResult)
    score = []
    for s in splitted:
        dart = int(''.join(re.compile('[0-9]+').findall(s)))
        bonus = re.compile('[A-Z]').findall(s)[0]
        option = re.compile('[*#]').findall(s)

        if bonus == 'D':
            dart = dart ** 2
        elif bonus == 'T':
            dart = dart ** 3
        
        if len(option) == 0:
            pass
        elif option[0] == '*':
            dart *= 2
            if len(score) >= 1:
                score[-1] *= 2
        elif option[0] == '#':
            dart *= -1
        
        score.append(dart)
        
    return(sum(score))

print(solution(''))
