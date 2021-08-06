def solution(price, money, count):
    total_count = int((count+1) * count / 2)
    
    return money - (price * total_count)