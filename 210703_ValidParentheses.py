class Solution:
    def isValid(self, s: str) -> bool:
        couples = {'(' : ')', '[' : ']', '{': '}'}
        open = ['(', '[', '{']
        close = [')', ']', '}']
        stack = []
        for p in s:
            if p in open:
                stack.append(p)
            else:
                try:
                    last_parenthesis = stack.pop()
                    if couples[last_parenthesis] == p:
                        continue
                    else:
                        return False
                except:
                    return False
        if len(stack) > 0 :
            return False
        return True

s = Solution()
print(s.isValid("()[]{}"))