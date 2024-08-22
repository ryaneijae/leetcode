class Solution(object):
    def isPalindrome(self, x):
        return x == x[::-1]

    """
    :type s: str
    :rtype: str
    """
    def longestPalindrome(self, s):
        longest = ''

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if j - i + 1 > len(longest):
                    testing = s[i:j]
                    if self.isPalindrome(testing):
                        if len(testing) > len(longest):
                            longest = testing
        return longest

        
