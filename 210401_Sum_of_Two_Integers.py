
'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Input: a = 1, b = 2
Output: 3
'''

class Solution():
    def getSum(self, a:int, b:int) -> int:
        return sum([a,b])

s = Solution()
print(s.getSum(1,2))