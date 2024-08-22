from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)
        for word in strs:
            my_key = ''.join(sorted(word))
            ans_dict[my_key].append(word)
        
        return ans_dict.values()
