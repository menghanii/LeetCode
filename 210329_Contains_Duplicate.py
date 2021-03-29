from typing import List
'''
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
'''

# class Solution(): # Time Limit Exceeded : O(N^2) ==> for(N) * in(N)
#     def containsDuplicate(self, nums:List[int]) -> bool:
#         bag = []
#         for i in nums:
#             if i in bag:
#                 return True
#             else:
#                 bag.append(i)
#         return False

class Solution(): # Success ==> sort(NlogN) + for(N) -> O(N)
    def containsDuplicate(self, nums:List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        else:
            return False

nums = [1, 2, 3, 4]
s = Solution()
print(s.containsDuplicate(nums))