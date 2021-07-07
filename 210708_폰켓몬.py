def solution(nums):
    answer = 0
    # find the number of unique ponkemons
    unique_num = len(set(nums))
    if unique_num >= (len(nums)/2) :
        answer = len(nums)/2
    else:
        answer = unique_num
    return answer

