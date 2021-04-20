# 점수 N의 자릿수는 항상 짝수 자릿수로만 주어짐.
score = input()
half = len(score)//2
left, right = list(map(int, score[:half])), list(map(int, score[half:]))
if sum(left) == sum(right):
    print('lucky')
else:
    print('ready')
