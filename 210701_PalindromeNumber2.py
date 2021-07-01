class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        denominator = 1
        forward = []
        while True:
            if x // denominator == 0:
                denominator = int(denominator / 10)
                break
            else:
                denominator *= 10
        while denominator >= 1:
            divnmod = divmod(x, denominator)
            forward.append(divnmod[0])
            x = divnmod[1]
            denominator = int(denominator / 10)
        reverse = forward[::-1]
        if reverse == forward:
            return True
        else:
            return False

s = Solution()
print(s.isPalindrome(123))