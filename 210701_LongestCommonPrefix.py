from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        shortest_len = len(sorted(strs, key=lambda x: len(x))[0])
        for i in range(shortest_len):
            prefix = []
            for string in strs:
                prefix.append(string[i])
            if len(set(prefix)) == 1:
                answer+=prefix[0]
            else:
                break
        return answer

s = Solution()
print(s.longestCommonPrefix(strs=["", ""]))
            
            
