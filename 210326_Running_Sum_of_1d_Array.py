from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum = 0
        result = []
        for i in nums:
            runsum += i
            result.append(runsum)
        return result

nums = [1, 2, 3, 4]
sol = Solution()
res = sol.runningSum(nums)
print(res)