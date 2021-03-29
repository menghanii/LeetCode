from typing import List
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_idx = 0
        max_price = 0
        min_idx = 0
        min_price = prices[0]
        profit_list = []
        for i in range(1, len(prices)):
            if prices[i] >= max_price: # max_price가 같은 경우라도 date를 나중으로 업데이트시켜줘야함.(> -> >=)
                # Edge Case : [2,1,2,1,0,1,2]
                max_price = prices[i]
                max_idx = i
            if prices[i] < min_price: # min_price는 같은 경우 앞 날짜를 유지시키는게 좋으므로, 더 낮은 경우가 아니면 업데이트 X. 
                min_price = prices[i]
                min_idx = i
            if max_idx > min_idx:
                profit_list.append(max_price - min_price)

            else: # Edge Case : [3,3,5,0,0,3,1,4]
                max_price = 0 # max_idx < min_idx 일때, max_price = 0으로 해서 다시 뒷 날짜의 max_price가 나오게끔 해야함. 
        if len(profit_list) == 0:
            return 0
        else:
            return max(profit_list)
s = Solution()
print(s.maxProfit([3,3,5,0,0,3,1,4]))