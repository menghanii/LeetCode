from typing import List
'''
Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''
# class Solution(): # Time Limit Exceeded
#     def product(self, lst:List[int]) -> int:
#         product = 1
#         for i in lst:
#             product *= i
#         return product
#     def productExceptSelf(self, nums:List[int]) -> List[int]:
#         answer = []
#         for _ in range(len(nums)):
#             pop = nums.pop(0)
#             product = self.product(nums)
#             answer.append(product)
#             nums.append(pop)
#         return answer

class Solution():
    def product(self, lst:List[int]) -> int:
        product = 1
        for i in lst:
            product *= i
        return product

    def productExceptSelf(self, nums:List[int]) -> List[int]:
        
        answer = []
        if nums.count(0) == 1:
            nums.remove(0)
            total_prod = 
        else:
            total_prod = self.product(nums)
        for i in range(len(nums)):
            if i == 0: # Edge Case : [-1, 1, 0, -3, 3]
                answer.append()
            else:
                answer.append(int(total_prod/i))
        return answer
        

nums = [1, 2, 3, 4]
s = Solution()
print(s.productExceptSelf(nums))


            