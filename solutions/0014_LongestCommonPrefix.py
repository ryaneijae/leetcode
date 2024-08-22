class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = None
        for each_str in strs:
            if ans == None:
                ans = each_str
            else:
                min_len = min(len(ans), len(each_str))
                new_ans = ''
                for i in range(min_len):
                    if ans[i] == each_str[i]:
                        new_ans += ans[i]
                    else:
                        break
                ans = new_ans
        return ans
        
