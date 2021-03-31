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
            if i == 0: # 미리 product 단계에서 0인 경우를 continue 시켜줘서 필요없는 연산을 없앤다.
                continue
            product *= i
        return product

    def productExceptSelf(self, nums:List[int]) -> List[int]:
        answer = []
        total_prod = self.product(nums)
        zero_cnt = 0
        zero_idx = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
                zero_idx.append(i)
                answer.append(0)
            else:
                answer.append(int(total_prod/nums[i]))

        if zero_cnt == 0:
            return answer
        elif zero_cnt == 1:
            answer = [0 for _ in range(len(nums)-1)]
            answer.insert(zero_idx[0], total_prod)
            return answer
        else:
            answer = [0 for _ in range(len(nums))]
            return answer


        # zero_cnt = nums.count(0)
        # if zero_cnt == 0: # Edge Case : [-1, 1, 0, -3, 3]
        #     for i in range(len(nums)):
        #         answer.append(int(total_prod/i))
        # elif zero_cnt == 1:
        #     nums.remove(0)
            
        # else:
        #     answer = [0] for _ in range(len(nums))
        
        return answer
        

nums = [1, 2, 3, 4]
s = Solution()
print(s.productExceptSelf(nums))


            