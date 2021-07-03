from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        for k, v in dic.items():
            if v == 1:
                return k
