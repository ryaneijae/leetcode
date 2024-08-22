class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }

        ans = None
        neg = False
        for i, c in enumerate(s):
            if ans == None:
                if c == '-':
                    neg = True
                    ans = 0
                elif c == '+':
                    ans = 0
                elif c == ' ':
                    continue
                elif c in digits:
                    ans = digits[c]
                else:
                    return 0
            else:
                if c in digits:
                    ans = 10 * ans + digits[c]
                else:
                    break
                    
        if ans == None:
            return 0        

        if neg:
            ans = -ans
        
        if ans < - 2**31:
            ans = -2**31
        if ans > 2**31 - 1:
            ans = 2**31 - 1

        return ans
