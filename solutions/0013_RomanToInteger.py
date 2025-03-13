class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        ans = 0
        prev = 0
        for i, c in enumerate(s):
            cur = dict_roman[c]
            if cur > prev:
                ans = ans + cur - 2 * prev
            else:
             ans += cur
            prev = cur
        return ans
