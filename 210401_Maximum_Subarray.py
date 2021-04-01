from typing import List
'''
Given an integer array nums, find the contiguous(연속적인) subarray (containing at least one number) which has the largest sum and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4] [1, 2, 3, 4, 5, 6] [-1, -2, -3, -4, -5, -6]
-2 -> -2 + 1
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

# Dynamic Programming 문제
# DP : 큰 문제를 작은 문제 여러 개로 나누어서 풀 때, 계속 풀어야되는 작은 문제의 값을 저장해두고 재사용하는 기법.
# Kadane's Algorithm.

class Solution():
    def maxSubArray(self, nums:List[int]) -> int:
        dp = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
    
        return max(dp)

s = Solution()
array1 = [-2,1,-3,4,-1,2,1,-5,4]
array2 = [5, 4, -1, 7, 8]
print(s.maxSubArray(array1))
        
