class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        if numRows == 1: return s
        if len(s) <= numRows: return s 
        interval = 2 * (numRows - 1)
        for i in range(0, len(s), interval):
            ans += s[i]
        for r in range(1, numRows - 1):
            i = r
            ans += s[i]
            i = interval
            while True:
                first = i - r
                second = i + r
                if first < len(s):
                    ans += s[first]
                else:
                    break
                if second < len(s):
                    ans += s[second]
                else:
                    break
                i += interval
        for i in range(numRows - 1, len(s), interval):
            ans += s[i]  
        return ans


