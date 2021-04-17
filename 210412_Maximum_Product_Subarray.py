from typing import List
'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [2,-2,3,4,-5]
Output: 12
[2, -2, 3,]
'''

class Solution:
    def maxProduct(self, nums:List[int]) -> int:
        prod = 1
        cnt = 0 # 0보다 작은 값의 개수가 홀수인지 짝수인지 확인
        for i in nums:
            if i < 0:
                cnt += 1
            prod *= i
        if cnt % 2 == 0: # 마이너스 개수가 짝수면
            return prod
        else:
            # 첫 번째와 마지막 번 째 수를 비교
            while True:
                first = nums.pop(0) 
                last = nums.pop()
                
s = Solution()
print(s.maxProduct([2,3,-2,4]))
        