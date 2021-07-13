import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) != 0:
        first_spicy = heapq.heappop(scoville)
        if first_spicy >= K:
            break
        else:
            if len(scoville) == 0:
                answer = -1
                break
            second_spicy = heapq.heappop(scoville)
            new_spice = first_spicy + (2*second_spicy)
            answer += 1
            heapq.heappush(scoville, new_spice)
    return answer   

print(solution([1, 1], 7))