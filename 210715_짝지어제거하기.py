# using regex - high time complexity
# import re
# def solution(s):
#     answer = 0
#     pattern = re.compile(r'([a-z])\1') # back reference - regex
#     while len(re.findall(pattern, s)) != 0:
#         s = re.sub(pattern, '', s)
    
#     if len(s) != 0:
#         return answer
#     else:
#         return 1

# use stack
def solution(s):
    answer = 0
    s = list(s)
    stack = [s.pop()]
    while len(s) != 0:
        a = s.pop()
        if len(stack) == 0:
            stack.append(a)
            continue
        b = stack.pop()
        if a != b:
            stack.append(b)
            stack.append(a)
    if len(stack) == 0:
        return 1
    return answer
print(solution('baacb'))
# what is edge case?
# time complexity between pop() and pop(0)