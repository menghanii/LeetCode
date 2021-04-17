'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# class Solution(): # 재귀 -> Time Limit Exceeded
#     def climbStairs(self, n:int) -> int:
#         # n = 1 : 1 step
#         # n = 2 : p1 + 2step
#         # n = 3 : 1계단 간 경우 -> n=2, 2계단 간 경우 -> n=1
#         # n = 4 : 1계단 간 경우 -> n=3, 2개단 간 경우 -> n=2  
#         # (n-2)번째 계단까지 가는 경우 * p2 + (n-1)번째 계단까지 가는 경우 * p1
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         else:
#             return self.climbStairs(n-1)  + self.climbStairs(n-2)

class Solution(): # DP
    def climbStairs(self, n:int) -> int:
        dp = [1, 2]
        for i in range(n-2):
            dp.append(dp[-2] + dp[-1]) # 피보나치 수열
        return dp[n-1] # ex) 3번째 index를 반환해야하므로 dp[2].

s = Solution()
print(s.climbStairs(4))