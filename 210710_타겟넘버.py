from itertools import combinations
# def solution(numbers, target): # numbers = [1,2,3,4,5]
#     for i in range(len(numbers)):
#     answer = 0
#     sum_list = [sum(numbers)]
#     for i in range(len(numbers)):
#         plus = numbers[:len(numbers)-(i+1)]
#         minus = [-j for j in numbers[len(numbers)-(i+1):]] # [-3, -4, -5]
#         print(plus)
#         print(minus)
#         while minus:
#             print(sum(plus) + sum(minus))
#             sum_list.append(sum(plus) + sum(minus))        
#             plus.append(minus.pop() * -1)
#         print()
#     return sum_list

# print(solution([1,2,3,4,5], 3))
numbers = [1,2,3,4,5]
for i in range(1, len(numbers)+1):
    combi = combinations([0,1,2,3,4], i)
    for c in combi:
        for i in range(len(c)):
            print(-1 * numbers[c[i]])
