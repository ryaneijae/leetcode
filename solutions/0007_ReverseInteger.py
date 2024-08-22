class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0: neg = True
        x = abs(x)
        ans = 0
        while x > 0:
            if ans > 0:
                ans = ans * 10
            ans += x % 10
            x = x // 10
        
        if neg:
            ans = - ans
        
        if ans < - 2**31:
            return 0
        elif ans > 2**31 - 1:
            return 0
        return ans
