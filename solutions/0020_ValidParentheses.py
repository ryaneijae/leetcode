class Solution:
    para = {'(': ')', '[':']', '{': '}'}
    
    def isValid(self, s: str) -> bool:
        if len(s) % 2: return False
        the_stack = []

        for c in s:
            if c in Solution.para:
                the_stack.append(c)
            else:
                if len(the_stack) == 0 or Solution.para[the_stack.pop()] != c:
                    return False
        return len(the_stack) == 0

