from typing import List

'''
exactly one solution!
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1): # 0, 1, 2
            me = nums[i]
            for j in range(i+1, len(nums)): 
                you = nums[j]
                if me + you == target:
                    return [i, j]

s = Solution()
print(s.twoSum([2,7,11,15], 9))